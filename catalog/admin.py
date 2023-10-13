from django.contrib import admin

from catalog.models import Category, Product, Contact, Message


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # поиск
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    # фильтрация
    list_filter = ('category',)
    # поиск
    search_fields = ('category', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'inn', 'address', 'phone')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'message')
    # фильтрация
    list_filter = ('name', 'phone', 'email',)
    # поиск
    search_fields = ('name', 'phone', 'email', 'message')
