from django.db import models
from products.models import Product

class Order(models.Model):
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200, null=False)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    uuid=models.BigIntegerField(null=True, blank=True, unique=True)
    payment=models.BooleanField(default=False, null=True, blank=True)
    create_date=models.DateTimeField(auto_now_add=True)
    price=models.PositiveIntegerField()

    def __str__(self):
        return f'Заказ номер {self.id}.    Получатель {self.first_name} {self.last_name}'


class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()

    def __str__(self):
        return f'Заказ {self.order.uuid}.   Название {self.product}'

