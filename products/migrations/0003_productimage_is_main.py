# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-07 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=True),
        ),
    ]