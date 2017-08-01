from django.views.generic import DetailView, ListView
from products.models import Product, ProductImage


class ProductView(DetailView):

    template_name = 'products/Product_view.html'
    model = Product

    def dispatch(self, request, *args, **kwargs):
        self.session_key = request.session.session_key
        if not self.session_key:
            request.session.cycle_key()
        return super(ProductView, self).dispatch(request, *args, **kwargs)


class CategoryView(ListView):

    template_name = 'products/Category_view.html'
    model = Product

    def dispatch(self, request, *args, **kwargs):
        self.pk = self.kwargs['pk']
        return super(CategoryView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ProductImage.objects.filter(product__category_id=self.pk)
        return queryset