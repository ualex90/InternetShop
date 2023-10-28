from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, PasswordRecoveryView, EmailVerifyView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/', EmailVerifyView.as_view(), name='email_verify'),
    path('password_recovery', PasswordRecoveryView.as_view(), name='password_recovery'),
]
