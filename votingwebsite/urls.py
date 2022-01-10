from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # disable x/ path during deployment
    path('x/', admin.site.urls),
    path('', views.FrontPage, name="frontpage"),
    path('auth/', include('authentication.urls')),
]
