from django import forms
from orders.models import Order


class FormOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'customer_phone', 'customer_address', 'comment')