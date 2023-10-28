from django.contrib.auth.forms import AuthenticationForm

from catalog.forms import StyleFrmMixin


class LoginForm(StyleFrmMixin, AuthenticationForm):
    pass
