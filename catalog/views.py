from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category, Contacts, Message


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Каталог товаров',
        'description': 'Категории',
    }


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = category_item.name
        context_data['description'] = category_item.description

        return context_data


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


def add_product(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image') if 'image' in request.FILES else None
        if image:
            fs = FileSystemStorage()
            fs.save(None, image)

        Product.objects.create(
            category_id=category_id,
            name=name,
            description=description,
            price=price,
            image=image,
        )

    category_list = Category.objects.all()
    context = {
        'title': 'Продукт',
        'description': 'Добавление нового продукта',
        'category_list': category_list,
    }
    return render(request, 'catalog/add_product.html', context)
