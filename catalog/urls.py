from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, product, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', ProductListView.as_view(), name='products'),
    path('product/<int:pk>', product, name='product'),
    path('add_product', add_product, name='add_product'),
]
