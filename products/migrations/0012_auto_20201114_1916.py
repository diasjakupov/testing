# Generated by Django 3.0.8 on 2020-11-14 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201110_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='product',
            name='price_with_dicount',
            field=models.FloatField(default=0, verbose_name='Цена со скидкой'),
        ),
    ]
