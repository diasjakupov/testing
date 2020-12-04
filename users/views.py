from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import User
from django.shortcuts import redirect
from .serializers import PublicUserSerializer
from rest_framework.reverse import reverse_lazy
from rest_framework.response import Response


class PublicUserViewSet(ModelViewSet):
    serializer_class = PublicUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        if user.privacy:
            raise Exception('this profile is private')
        return user
