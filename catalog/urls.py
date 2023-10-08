from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import categories, contacts, products, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', categories, name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/product/', product, name='product'),
]
