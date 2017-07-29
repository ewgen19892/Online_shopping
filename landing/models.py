from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, blank=True, null=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    published = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.name