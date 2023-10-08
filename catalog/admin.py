from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
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


@admin.register(Contacts)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'inn', 'address',)
