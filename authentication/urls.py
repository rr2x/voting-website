from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name="auth-url"),
    path('login', views.login, name="auth-login-url"),
    path('signup', views.signup, name="auth-signup-url"),
    path('resetpassword', views.resetpassword, name="auth-resetpassword-url"),
    path('logout', views.logout, name="auth-logout-url"),
]
