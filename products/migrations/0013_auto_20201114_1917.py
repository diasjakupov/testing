# Generated by Django 3.0.8 on 2020-11-14 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20201114_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_with_dicount',
            new_name='price_with_discount',
        ),
    ]
