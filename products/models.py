from django.db import models
from django.core.validators import MaxValueValidator


def get_foldername_for_productimage(instance, filename):
    return f'products/{instance.product.name}/{filename}'


def get_foldername_for_categoryimage(instance, filename):
    return f'category/{instance.name}/{filename}'


class TypeOfProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(
        upload_to=get_foldername_for_categoryimage, verbose_name="Фото для категории", null=True, blank=True, default='default/default.jpeg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = "Тип"


class SubCategory(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Под-категория'
        verbose_name_plural = "Под-категории"


class Product(models.Model):
    typeof = models.ManyToManyField(
        TypeOfProduct, verbose_name="Тип продукта", related_name='products')
    subcategory = models.ManyToManyField(SubCategory, related_name='products')
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(default=0, verbose_name="Цена")
    available = models.PositiveIntegerField(
        default=0, verbose_name="Доступно сейчас")
    discount=models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    price_with_discount=models.FloatField(default=0, verbose_name="Цена со скидкой")

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        disc=1-(self.discount/100)
        print(disc)
        self.price_with_discount=round(self.price*disc)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"


class Characteristic(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="characteristics")
    name = models.CharField(max_length=255, verbose_name="Название")
    value = models.CharField(max_length=300, verbose_name="Значение")
    suffix = models.CharField(max_length=100, verbose_name='Единица измерения')

    def __str__(self):
        return f'name:{self.name}, id:{self.id}'

    class Meta:
        verbose_name = 'Характеристика продукта'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_foldername_for_productimage)

    def __str__(self):
        return f'Фото для {self.product.name}'
