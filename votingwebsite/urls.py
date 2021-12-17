from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # TODO: remove this path on deployment
    path('x/', admin.site.urls),
    path('', include('authentication.urls')),
]
