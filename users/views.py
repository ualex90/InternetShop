from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

import users
from users.forms import LoginForm, RegisterForm, UserProfileForm
from users.models import User
from users.utils import get_user_key, get_password


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_verify')

    def form_valid(self, form):
        key = get_user_key()
        self.object = form.save()
        self.object.key = key
        self.object.save()
        send_mail(
            subject='подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: '
                    f'http://127.0.0.1:8000/users/email_verify/?key={key}',
            from_email=None,
            recipient_list=[self.object.email],
        )
        return super().form_valid(form)


class EmailVerifyView(TemplateView):
    template_name = 'users/user_verification.html'
    extra_context = {
        'title': 'Подтверждение регистрации',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.request.GET.get('key')

        # Если в запросе есть 'key', то выполняем верификацию
        if key:
            try:
                user = User.objects.get(key=key)
            except users.models.User.DoesNotExist:
                context['description'] = 'Пользователь не существует'
            else:
                user.is_active = True
                user.save()
                context['description'] = 'Спасибо за успешную регистрацию!'
                context['verify'] = True
            finally:
                return context

        # Если нет ключа, то предложим пользователю заглянуть в свою почту
        context['description'] = 'Для подтверждения регистрации перейдите по ссылке отправленной на Ваш email'
        context['register_end'] = True
        return context


class PasswordRecoveryView(TemplateView):
    template_name = 'users/reset_password.html'
    extra_context = {
        'title': 'Восстановление пароля',
    }

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        email = self.request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except users.models.User.DoesNotExist:
            context['description'] = 'Неверный email. Попробуйте еще раз'
        else:
            password = get_password()
            user.set_password(password)
            user.save()
            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {password}',
                from_email=None,
                recipient_list=[email],
            )

            return redirect(reverse('users:login'))
        return self.render_to_response(context)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'title': 'Профиль',
        'description': 'Редактировать профиль пользователя',
    }

    def get_object(self, queryset=None):
        return self.request.user
