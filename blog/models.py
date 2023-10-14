from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='превью', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.created_at} {self.title}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
