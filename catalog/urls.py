from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/<int:pk>', ProductListView.as_view(), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/create_product', ProductCreateView.as_view(), name='create_product'),
    path('product/update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
