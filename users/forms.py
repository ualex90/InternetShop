from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from catalog.forms import StyleFrmMixin
from users.models import User


class LoginForm(StyleFrmMixin, AuthenticationForm):
    pass


class RegisterForm(StyleFrmMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
