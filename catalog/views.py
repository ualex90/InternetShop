from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductVersionForm
from catalog.models import Product, Category, Message, Contact, ProductVersion
from catalog.services import get_object_list


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Каталог товаров',
        'description': 'Категории',
    }

    def get_queryset(self):
        # возвращаем кэшированный queryset, который присвоится к object_list
        return get_object_list(self.model)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk')).filter(is_published=True)
        # Пройдемся по всем выбранным продуктам
        for item in queryset:
            # Отфильтруем версии по продукту и признаку активности
            version = ProductVersion.objects.filter(product_id=item.pk).filter(is_active=True)
            # Если есть активная версия продукта, то добавим ее в аттрибут "version"
            item.version = version[0] if version else None
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = category_item.name
        context_data['description'] = category_item.description

        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.objects = super().get_object(queryset)
        self.objects.views_count += 1
        self.objects.save()
        return self.objects

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.category
        context_data['description'] = product_item.name

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Продукт',
        'description': 'Добавление нового продукта',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductVersionFormset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormset(self.request.POST)
        else:
            context_data['formset'] = ProductVersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:products_user')


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    extra_context = {
        'title': 'Редактирование',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['description'] = f'Изменить "{product_item.name}"'

        ProductVersionFormset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductVersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def has_permission(self):
        # Проверяем, является ли пользователь владельцем продукта, если да, то разрешаем редактирование
        if self.model.objects.get(pk=self.kwargs.get('pk')).owner == self.request.user:
            return True
        # если не является, то следуем ограничениям прав 'catalog.change_product'
        return super().has_permission()

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    extra_context = {
        'title': 'Удаление',
        'description': 'Удаление продукта',
    }

    def get_success_url(self):
        return reverse('catalog:products_user')

    def has_permission(self):
        # Проверяем, является ли пользователь владельцем продукта, если да, то разрешаем удаление
        if self.model.objects.get(pk=self.kwargs.get('pk')).owner == self.request.user:
            return True
        # если не является, то следуем ограничениям прав 'catalog.delete_product'
        return super().has_permission()


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


class ProductModeratorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'catalog.set_published'
    model = Product
    template_name = 'catalog/product_list.html'
    queryset = Product.objects.filter().filter().order_by('is_published')
    extra_context = {
        'title': 'Продукты',
        'description': 'Модерация продуктов',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        # Пройдемся по всем выбранным продуктам
        for item in queryset:
            # Отфильтруем версии по продукту и признаку активности
            version = ProductVersion.objects.filter(product_id=item.pk).filter(is_active=True)
            # Если есть активная версия продукта, то добавим ее в аттрибут "version"
            item.version = version[0] if version else None
        return queryset


@login_required
@permission_required('catalog.set_published')
def published(request, pk):
    post_item = get_object_or_404(Product, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:product', args=[pk]))


class ProductUserListView(LoginRequiredMixin, ListView):
    permission_required = 'catalog.set_published'
    model = Product
    template_name = 'catalog/product_list.html'
    extra_context = {
        'title': 'Продукты',
        'description': 'Мои продукты',
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)

        # Пройдемся по всем выбранным продуктам
        for item in queryset:
            # Отфильтруем версии по продукту и признаку активности
            version = ProductVersion.objects.filter(product_id=item.pk).filter(is_active=True)
            # Если есть активная версия продукта, то добавим ее в аттрибут "version"
            item.version = version[0] if version else None
        return queryset
