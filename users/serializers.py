from .models import User
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'is_staff',
            'is_active',
            'password',
            'is_superuser',
            'user_permissions',
            'groups',
            'privacy']
        read_onlu_fields = ['date_joined',
                            'personal_discount',
                            'total_sum',
                            'last_login']


class PublicUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'is_staff',
            'is_active',
            'password',
            'is_superuser',
            'user_permissions',
            'groups',
            'phone',
            'privacy',
            'email',
            'last_login',
            'total_sum')
        read_onlu_fields = ('date_joined', 'personal_discount')
