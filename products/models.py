from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Category: %s' % self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Product: %s' % self.name

    def get_short_test(self):
        if len(self.description) > 200:
            return self.description[:200]
        else:
            return self.description

    def save(self, *args, **kwargs):
        if self.discount != 0:
            self.price_with_discount = self.price - (self.price/100*self.discount)
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.product.name
