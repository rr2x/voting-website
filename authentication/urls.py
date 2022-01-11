from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcometoauth, name="auth-welcometoauth"),
    path('login', views.login, name="auth-login"),
]
