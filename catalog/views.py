from pathlib import Path
from datetime import datetime as dt

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Каталог товаров',
        'description': 'Комплектующие для умных систем',
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
