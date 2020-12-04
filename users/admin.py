from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin, UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('image', 'phone',
                                      'first_name', 'last_name', 'email', 'privacy')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(User, CustomUserAdmin)
