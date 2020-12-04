from decimal import Decimal
from shop import settings
from products.models import Product
from .serialiazers import ProductDetailSerializer


class Cart:
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        print(request.session)
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for item in self.cart.values():
            yield item

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product['id'])
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        if self.cart[product_id]['quantity']==0:
            self.remove(product)

        product=Product.objects.prefetch_related('images').get(id=int(product_id))
        self.cart[product_id]['product']=ProductDetailSerializer(product).data
        self.cart[product_id]['price_with_discount']=ProductDetailSerializer(product).data['price_with_discount']
        self.cart[product_id]['total_price']=self.cart[product_id]['price_with_discount']*self.cart[product_id]['quantity']
        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product['id'])
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
   

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(float(item['product']['price_with_discount']) * item['quantity'] for item in
                self.cart.values())
    
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

