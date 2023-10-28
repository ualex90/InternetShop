import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(**NULLABLE, max_length=35, verbose_name='номер телефона')
    country = models.CharField(**NULLABLE, max_length=50, verbose_name='страна')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватар')
    key = models.CharField(**NULLABLE, max_length=25, unique=True, verbose_name='ключ пользователя')
    is_active = models.BooleanField(default=False, verbose_name='активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
