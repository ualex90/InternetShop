from pathlib import Path
from datetime import datetime as dt

from django.shortcuts import render

from catalog.models import Product, Category


def categories(request):
    object_list = Category.objects.all()
    context = {
        'title': 'Каталог товаров',
        'description': 'Категории',
        'category_list': object_list,
    }
    return render(request, 'catalog/index.html', context)


def products(request, pk):
    category_item = Category.objects.get(pk=pk)
    object_list = Product.objects.filter(category_id=pk)
    context = {
        'title': category_item.name,
        'description': category_item.description,
        'product_list': object_list,
    }
    return render(request, 'catalog/index.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'title': 'товар',
        'description': product_item.name,
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # формирование сообщения
        time = dt.now()
        message = {str(time.isoformat()): {'name': name, 'phone': phone, 'message': message}}

    context = {
        'title': 'Контакты',
        'description': 'Наши адреса',
    }
    return render(request, 'catalog/contacts.html', context)

