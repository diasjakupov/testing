from django.contrib import admin
from .models import Product, ProductImage, Characteristic, TypeOfProduct, SubCategory


@admin.register(TypeOfProduct)
class TypeOfProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CharacteristicAdmin(admin.TabularInline):
    model = Characteristic
    extra = 1


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'available']
    inlines = [CharacteristicAdmin, ProductImageAdmin]


admin.site.register(Characteristic)
admin.site.register(SubCategory)
