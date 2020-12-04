from django.contrib import admin
from .models import OrderItem, Order

class OrderItemAdmin(admin.ModelAdmin):
    search_fields=('order__uuid',)
    list_display=['__str__', 'amount', 'total_price']


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order)

