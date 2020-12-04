import django_filters
from .models import Product, Characteristic, SubCategory


class InFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class CustomFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


def filter_by_characteristics(queryset, name, value):
    filter_name = name
    filter_args = [(value[i], value[i + 1], value[i + 2])
                   for i in range(0, len(value), 3)]
    filtered_queryset = queryset
    for filter in filter_args:
        filtered_queryset = filtered_queryset.filter(
            characteristics__name=filter[0],
            characteristics__value=filter[1],
            characteristics__suffix=filter[2])
    return filtered_queryset


class ProductFilter(django_filters.FilterSet):
    typeof = InFilter(field_name='typeof__name', lookup_expr='in')
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['typeof', 'name']


class CharacteristicFilter(django_filters.FilterSet):
    typeofproduct = InFilter(
        field_name='typeofproduct__name', lookup_expr='in')

    class Meta:
        model = Characteristic
        fields = ['typeofproduct']


class SubCategoryFilter(django_filters.FilterSet):
    typeof = InFilter(field_name='typeofproduct__name', lookup_expr='in')

    class Meta:
        model = SubCategory
        fields = ['typeof']
