from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import categories, contacts, products, product, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', categories, name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', products, name='products'),
    path('product/<int:pk>', product, name='product'),
    path('add_product', add_product, name='add_product'),
]
