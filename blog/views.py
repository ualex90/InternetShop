from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Блог',
        'description': 'Наши события'
    }


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        post_item = Post.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = post_item.title
        context_data['description'] = post_item.title

        return context_data


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'image', 'is_published']
    extra_context = {
        'title': 'Новая запись',
        'description': 'Создание новой записи в блог'
    }

    def get_success_url(self):
        # return reverse('blog:blog', args=[self.object.pk])
        return reverse('blog:blog')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'image', 'is_published']
    extra_context = {
        'title': 'Новая запись',
        'description': 'Создание новой записи в блог'
    }

    def get_success_url(self):
        return reverse('blog:post', args=[self.object.pk])


class PostDeleteView(DeleteView):
    model = Post
    extra_context = {
        'title': 'Удаление',
        'description': 'Удаление записи',
    }

    def get_success_url(self):
        return reverse('blog:blog')
