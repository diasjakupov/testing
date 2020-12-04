from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .cart import Cart
from products.models import Product
from .models import Order, OrderItem
from .serialiazers import CartSerializer, ProductDetailSerializer


import random

class CartView(APIView):
    def get(self, request, *agrs, **kwargs):
        cart=Cart(request)
        return Response(data={'cart':cart, 'total':cart.get_total_price()})

    def put(self, request, *args, **kwargs):
        data=request.data
        cart=Cart(request)
        """
"id":2, "remove":0,"quantity":1, "update_quantity":0
        """
        if data['remove'] or data['quantity']==0:
            cart.remove(data)
        else:
            cart.add(
                product=data,
                quantity=data['quantity'],
                update_quantity=data['update_quantity']
            )

        return Response(data={'cart':cart, 'total':cart.get_total_price()})

    def delete(self, request, *args, **kwargs):
        cart=Cart(request)
        cart.clear()
        return Response()

    
    def post(self, request, *args, **kwargs):
        print('posting')
        cart=Cart(request)
        print('posting')
        personal_data=request.data
        """
{
"phone": "87712841851",
"address":" Улица Пушкина",
"email": "dzhakupova.a@mail.ru",
"first_name": "Dias",
"last_name": "Jakupov"
}
        """
        if cart.get_total_price()!=0:
            uuid=random.sample(range(10**6, 10**9), 1)[0]
            while Order.objects.filter(uuid=uuid).exists():
                uuid=random.sample(range(10**6, 10**9), 1)[0]
            else:
                order=Order.objects.create(
                    phone=personal_data['phone'],
                    address=personal_data['address'],
                    email=personal_data['email'],
                    first_name=personal_data['first_name'],
                    last_name=personal_data['last_name'],
                    price=cart.get_total_price(),
                    uuid=uuid
                )
            
            for item in cart:
                orderitem_data=dict(item.items())
                OrderItem.objects.create(
                    product=Product.objects.get(id=int(orderitem_data['product']['id'])),
                    order=order,
                    amount=orderitem_data['quantity'],
                    total_price=orderitem_data['total_price']
                    )

            cart.clear()
            return Response({'cart':cart, 'uuid':order.uuid})
        else:
            raise Exception('Корзина не должна быть пустая')
            
        
        



