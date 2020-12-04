from rest_framework import serializers
from .models import Product, Characteristic, TypeOfProduct, ProductImage, SubCategory


class TypeOfProductListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = TypeOfProduct
        fields = ['name', 'count', 'image']

    def get_count(self, obj):
        return obj.products.all().count()


class TypeOfProductForProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfProduct
        fields = ['name']


class SubCategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ['name', 'count']

    def get_count(self, obj):
        return obj.products.all().count()


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class CharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic
        fields = ['name', 'value', 'suffix']


class ProductDetailSerializer(serializers.ModelSerializer):
    typeof = TypeOfProductForProductListSerializer()
    subcategory=SubCategorySerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['typeof', 'name', 'description',
                  'price', 'available', 'images', 'characteristics', 'subcategory', ]



class ProductListSerializer(serializers.ModelSerializer):
    typeof = TypeOfProductForProductListSerializer(many=True)
    images = ProductImageSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    subcategory = SubCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id','name', 'price', 'images', 'typeof',
                  'subcategory', 'characteristics', 'description','discount','price_with_discount']
