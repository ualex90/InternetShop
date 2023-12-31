import random

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE

COUNTRY_CHOICES = {
    ('RU', 'Россия'),
    ('AM', 'Армения'),
    ('BY', 'Беларусь'),
    ('GE', 'Грузия'),
    ('KZ', 'Казахстан'),
    ('KG', 'Киргизия'),
    ('LV', 'Латвия'),
    ('LT', 'Литва'),
    ('MD', 'Молдова'),
    ('CK', 'Острова Кука'),
    ('UZ', 'Узбекистан'),
    ('OS', 'Южная Осетия'),
    ('XX', 'Другая страна'),
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    first_name = models.CharField(**NULLABLE, max_length=35, verbose_name='Имя')
    last_name = models.CharField(**NULLABLE, max_length=35, verbose_name='Фамилия')
    phone = models.CharField(**NULLABLE, max_length=35, verbose_name='номер телефона')
    country = models.CharField(**NULLABLE, max_length=25, choices=COUNTRY_CHOICES, verbose_name='страна')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватар')
    key = models.CharField(**NULLABLE, max_length=25, unique=True, verbose_name='ключ пользователя')
    is_active = models.BooleanField(default=False, verbose_name='активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
