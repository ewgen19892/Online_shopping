from .models import ProductInBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_price = 0
    for product_in_basket in products_in_basket:
        products_total_price += product_in_basket.total_price

    return locals()
