from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

import users
from users.forms import LoginForm, RegisterForm
from users.models import User
from users.utils import get_user_key


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:categories')

    def form_valid(self, form):
        key = get_user_key()
        self.object = form.save()
        self.object.key = key
        self.object.save()

        send_mail(
            subject='подтверждение регистрации',
            message=f'код авторизации {key}',
            from_email=None,
            recipient_list=[self.object.email],
        )
        return super().form_valid(form)


def email_verify(request, key):
    context = dict()
    try:
        user = User.objects.get(key=key)
    except users.models.User.DoesNotExist:
        context = {
            'title': 'Подтверждение регистрации',
            'description': 'Пользователь не существует',
            'verify': False,
        }
    else:
        user.is_active = True
        user.save()
        context = {
            'title': 'Подтверждение регистрации',
            'description': 'Спасибо за успешную регистрацию!',
            'verify': True,
        }
    finally:
        return render(request, 'users/user_verification.html', context)

