from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'is_published', 'title', 'view_count', )
    list_filter = ('is_published',)
    search_fields = ('title', 'body',)
