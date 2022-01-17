from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):

        user = User.objects.get(email=username)

        if not user:
            return None

        if not check_password(password, user.password):
            return None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
