from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductModeratorListView, published, ProductUserListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/<int:pk>/', ProductListView.as_view(), name='products'),  # never_cache(ProductListView.as_view())
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/create_product/', ProductCreateView.as_view(), name='create_product'),
    path('product/<int:pk>/update_product/', ProductUpdateView.as_view(), name='update_product'), # never_cache(ProductUpdateView.as_view())
    path('product/<int:pk>/delete_product/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/', ProductModeratorListView.as_view(), name='products_moderator'),
    path('publised/<int:pk>/', published, name='published'),
    path('products/user/', ProductUserListView.as_view(), name='products_user'),
]
