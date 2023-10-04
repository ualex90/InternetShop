from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    # поиск
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    # фильтрация
    list_filter = ('category',)
    # поиск
    search_fields = ('category', 'product_description',)
