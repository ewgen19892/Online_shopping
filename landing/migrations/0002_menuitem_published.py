# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
