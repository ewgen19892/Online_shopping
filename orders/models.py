import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Status: %s' % self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_number = models.CharField(max_length=10, default=0)
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Order: %s %s %s' % (self.id, self.customer_name, self.customer_email)

    def save(self, *args, **kwargs):
        self.order_number = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                                    for x in range(6))
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    def save(self, *args, **kwargs):
        if self.product.discount != 0:
            price_per_item = self.product.price_with_discount
            self.price_per_item = price_per_item
            self.total_price = int(self.number) * self.price_per_item
        else:
            price_per_item = self.product.price
            self.price_per_item = price_per_item
            self.total_price = int(self.number) * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for product in all_products_in_order:
        order_total_price += product.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=120)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #number*price
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name

    def save(self, *args, **kwargs):
        if self.product.discount != 0:
            price_per_item = self.product.price_with_discount
            self.price_per_item = price_per_item
            self.total_price = int(self.number) * self.price_per_item
        else:
            price_per_item = self.product.price
            self.price_per_item = price_per_item
            self.total_price = int(self.number) * self.price_per_item
        super(ProductInBasket, self).save(*args, **kwargs)