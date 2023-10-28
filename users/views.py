from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render

from users.forms import LoginForm


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(BaseLogoutView):
    pass
