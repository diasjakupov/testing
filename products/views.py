from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .filters import ProductFilter, CharacteristicFilter, SubCategoryFilter


class ProductViewSet(ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        qs = Product.objects.prefetch_related(
            'images', 'characteristics', 'typeof',
            'subcategory', 'subcategory__products').all()
        return qs

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        elif self.action == 'list':
            return ProductListSerializer




class CharacteristicViewSet(ModelViewSet):
    queryset = Characteristic.objects.prefetch_related('typeofproduct').all()
    serializer_class = CharacteristicSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CharacteristicFilter


class TypeOfProductViewSet(ModelViewSet):
    queryset = TypeOfProduct.objects.all().prefetch_related('products')
    serializer_class = TypeOfProductListSerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all().prefetch_related('products', 'typeofproduct')
    serializer_class = SubCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubCategoryFilter
