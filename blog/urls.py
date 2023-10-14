from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostUpdateView, PostDetailView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    ]
