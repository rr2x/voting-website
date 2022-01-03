from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('x/', admin.site.urls),
    path('', views.FrontPage, name="frontpage"),
    path('auth/', include('authentication.urls')),
]
