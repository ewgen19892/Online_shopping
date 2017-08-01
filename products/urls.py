from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', ProductView.as_view(), name='show_product'),
    url(r'^products/(?P<pk>\d+)/$', CategoryView.as_view(), name='category'),
]
