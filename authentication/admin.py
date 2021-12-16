from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


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

    list_display = ('email', 'is_verified', 'last_login', 'created_at',)
    list_filter = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_verified')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_verified'),
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
