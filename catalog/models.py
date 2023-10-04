from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
