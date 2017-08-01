from django.views.generic import ListView
from products.models import ProductImage


class HomeView(ListView):

    template_name = 'landing/Home.html'
    model = ProductImage
    queryset = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by('-created')[:4]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['product_images_discount'] = ProductImage.objects.filter(is_active=True, is_main=True,
                                                                         product__is_active=True).exclude(product__discount=0)[:8]
        return context
