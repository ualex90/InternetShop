from django.contrib.auth.forms import AuthenticationForm
from django.forms import CheckboxInput

from catalog.forms import StyleFrmMixin


class LoginForm(StyleFrmMixin, AuthenticationForm):
    pass
