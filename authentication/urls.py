from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcometoauth, name="auth-welcometoauth"),
    path('login', views.login, name="auth-login"),
    path('signup', views.signup, name="auth-signup"),
    path('resetpassword', views.resetpassword, name="auth-resetpassword"),
]
