from django.shortcuts import render

from catalog.models import Product, Category, Contacts, Message


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
        'title': product_item.category,
        'description': product_item.name,
        'product': product_item,
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        message = {'name': name, 'phone': phone, 'email': email, 'message': message}
        Message.objects.create(**message)

    contact_list = Contacts.objects.all()
    context = {
        'title': 'Контакты',
        'description': 'Наши адреса',
        'contact_list': contact_list,
    }
    return render(request, 'catalog/contacts.html', context)

