from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('x/', admin.site.urls),
    path('', include('authentication.urls')),
]
