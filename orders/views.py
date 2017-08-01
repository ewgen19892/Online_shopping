from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, TemplateView
from orders.forms import FormOrder
from orders.models import *


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).delete()
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={'number': nmb}, order__isnull=True)
        if not created:
            new_product.number += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    return_dict['products_total_nmb'] = products_total_nmb
    return_dict['products'] = list()

    products_total_price = 0
    for product_in_basket in products_in_basket:
        products_total_price += product_in_basket.total_price
        product_dict = dict()
        product_dict['name'] = product_in_basket.product.name
        product_dict['price_per_item'] = product_in_basket.price_per_item
        product_dict['nmb'] = product_in_basket.number
        product_dict['id'] = product_in_basket.id
        product_dict['total_price'] = product_in_basket.total_price
        return_dict['products_total_price'] = products_total_price
        return_dict['products'].append(product_dict)
    return JsonResponse(return_dict)


class ProductInBasketView(ListView, FormView):
    template_name = 'orders/Checkout.html'
    model = ProductInBasket
    form_class = FormOrder

    def dispatch(self, request, *args, **kwargs):
        self.session_key = request.session.session_key
        return super(ProductInBasketView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ProductInBasket.objects.filter(session_key=self.session_key, is_active=True, order__isnull=True)
        return queryset

    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data['customer_name']
        email = data['customer_email']
        phone = data['customer_phone']
        address = data['customer_address']
        comment = data['comment']
        user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
        order = Order.objects.create(user=user, customer_name=name, customer_email=email, customer_phone=phone,
                                     customer_address=address, comment=comment, status_id=2)
        for key, value in data.items():
            if key.startswith('product_in_basket_'):
                product_in_basket_id = key.split('product_in_basket_')[1]
                product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                product_in_basket.number = value
                product_in_basket.order = order
                product_in_basket.save(force_update=True)
                ProductInOrder.objects.create(product=product_in_basket.product, number=product_in_basket.number,
                                              price_per_item=product_in_basket.price_per_item,
                                              total_price=product_in_basket.total_price, order=order)
        return HttpResponseRedirect('/thx/')


class DeleteProductInBasket(DeleteView):
    model = ProductInBasket
    success_url = reverse_lazy('checkout')


class OrderStatus(TemplateView):
    template_name = 'orders/Track_order.html'

    def dispatch(self, request, *args, **kwargs):
        self.search = request.GET.get('search')
        return super(OrderStatus, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderStatus, self).get_context_data(**kwargs)
        if self.search:
            try:
                context['status_order'] = Order.objects.get(order_number=self.search)
            except:
                context['status_order'] = 'Order not found'
        return context