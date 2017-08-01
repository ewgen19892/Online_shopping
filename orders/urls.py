from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView
from orders.views import *

urlpatterns = [
    url(r'^basket_adding/$', basket_adding, name='basket_adding'),
    url(r'^checkout/$', ProductInBasketView.as_view(), name='checkout'),
    url(r'^thx/$', TemplateView.as_view(template_name='orders/Thx.html'), name='thx'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteProductInBasket.as_view(), name='delete'),
    url(r'^track/$', OrderStatus.as_view(), name='status'),

]
