from django.urls import path, include, re_path
from .views import ProductViewSet, CharacteristicViewSet, TypeOfProductViewSet, SubCategoryViewSet

urlpatterns = [
    path('<int:pk>', ProductViewSet.as_view(
        {'get': 'retrieve'})),
    path('', ProductViewSet.as_view(
        {'get': 'list'})),
    path('characteritics', CharacteristicViewSet.as_view({'get': 'list'})),
    path('type', TypeOfProductViewSet.as_view({'get': 'list'})),
    path('subcategory', SubCategoryViewSet.as_view({'get': 'list'}))

]
