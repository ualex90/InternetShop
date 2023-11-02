from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostEditListView, PostListView, PostUpdateView, PostDetailView, PostDeleteView, \
    published

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('edit_list/', PostEditListView.as_view(), name='edit_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create'),  # never_cache(PostCreateView.as_view())
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),  # never_cache(PostUpdateView.as_view())
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('published/<int:pk>/', published, name='published'),
]
