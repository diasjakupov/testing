from rest_framework import serializers
from products.models import Product, Characteristic, TypeOfProduct, ProductImage, SubCategory
from products.serializers import ProductImageSerializer
from .models import Order


class ProductDetailSerializer(serializers.ModelSerializer):
    images=ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['name', 'images',
                  'price', 'price_with_discount','id']



class CartSerializer(serializers.Serializer):
    price=serializers.FloatField()
    product=ProductDetailSerializer()




