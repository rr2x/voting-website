from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# create and update form similar in nature
class UserForm(forms.ModelForm):

    # show hash on edit mode
    password = ReadOnlyPasswordHashField(
        label=("Current Password"), help_text=(
            "Passwords are securely hashed. "
            "Cannot be decrypted."
        ),)

    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords does not match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    form = UserForm
    add_form = UserForm

    list_display = ('email', 'is_verified', 'last_login', 'created_at',)
    list_filter = ('email',)

    # edit mode
    fieldsets = (
        (None, {'fields': ('email', 'password',
         'password1', 'password2', 'is_verified')}),
    )

    # add mode
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_verified'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    # hide superuser from list of users
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
