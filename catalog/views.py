from pathlib import Path
from datetime import datetime as dt

from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'title': 'Каталог товаров',
        'description': 'Комплектующие для умных систем',
        'product_list': product_list,
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


def product(request):
    context = {
        'title': 'товар',
        'description': 'Описание',
    }
    return render(request, 'catalog/includes/inc_product_card.html', context)
