from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, ProductImage


class HomeView(ListView):

    template_name = 'landing/Home.html'
    model = ProductImage
    queryset = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
        context['product_images_phones'] = product_images.filter(product__category__id=8)
        context['product_images_laptop'] = product_images.filter(product__category__id=9)
        return context
