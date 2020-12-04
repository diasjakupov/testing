from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


def DefineUserPathImages(instance, filename):
    return f'users/{instance.username}/{filename}'


class User(AbstractUser):
    image = models.ImageField(
        upload_to=DefineUserPathImages,
        null=True,
        blank=True,
        default='default/def.jpg')
    phone = models.CharField(max_length=18, null=True, blank=True)
    privacy = models.BooleanField(default=False)
    personal_discount = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(100)
    ])
    # //TODO create method for auto-fill this field
    total_sum = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
