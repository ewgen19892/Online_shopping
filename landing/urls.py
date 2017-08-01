from django.conf.urls import url
from django.views.generic import TemplateView, ListView

from landing.views import HomeView
from products.models import Product
from . import views

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^About/$', TemplateView.as_view(template_name='landing/About.html'), name='about'),

]

