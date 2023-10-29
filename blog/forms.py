from django import forms

from blog.models import Post
from catalog.forms import StyleFrmMixin


class PostForm(StyleFrmMixin, forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'is_published']
