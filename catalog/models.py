from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    image = models.ImageField(verbose_name='Превью', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    inn = models.IntegerField(verbose_name='ИНН')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=50, verbose_name='Телефон')

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='email')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщение'


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.SmallIntegerField(verbose_name='номер')
    name = models.CharField(max_length=25, verbose_name='название')
    is_active = models.BooleanField(default=False, verbose_name='текущая')

    def __str__(self):
        return f'v.{self.number} ({self.name})'

    class Meta:
        verbose_name = 'версию'
        verbose_name_plural = 'версии'
