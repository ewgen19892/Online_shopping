from django import template
from products.models import ProductCategory

register = template.Library()


@register.inclusion_tag('landing/Main_menu.html')
def top_menu():
    items = ProductCategory.objects.filter(is_active=True)
    return {'items': items}