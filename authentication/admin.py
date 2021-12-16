from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# current problem:
# OperationalError at /admin/authentication/user/1/change/
# no such table: authentication_user_groups

# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
