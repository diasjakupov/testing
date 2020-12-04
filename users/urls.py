from django.urls import path, include
from .views import PublicUserViewSet

urlpatterns = [
    path('public/<int:pk>', PublicUserViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
