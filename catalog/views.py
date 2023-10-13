from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Category, Message, Contact


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


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.category
        context_data['description'] = product_item.name

        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('category', 'name', 'description', 'price', 'image')
    extra_context = {
        'title': 'Продукт',
        'description': 'Добавление нового продукта',
    }

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('category', 'name', 'description', 'price', 'image')
    extra_context = {
        'title': 'Продукт',
        'description': 'Добавление нового продукта',
    }

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {
        'title': 'Удаление',
        'description': 'Удаление продукта',
    }

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])


class ContactView(TemplateView):
    template_name = 'catalog/contact_view.html'
    extra_context = {
        'title': 'Контакты',
        'description': 'Наши адреса',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Contact.objects.all()
        return context_data

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        name = self.request.POST.get('name')
        phone = self.request.POST.get('phone')
        email = self.request.POST.get('email')
        message = self.request.POST.get('message')
        Message.objects.create(name=name, phone=phone, email=email, message=message)
        return self.render_to_response(context)
