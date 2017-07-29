# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_main',
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]