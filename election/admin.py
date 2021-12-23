from django.contrib import admin
from .models import Election, ElectionInvite


class ElectionAdmin(admin.ModelAdmin):
    # TODO: Created By, remove superuser
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)


class ElectionInviteAdmin(admin.ModelAdmin):
    # TODO: Sent to, remove superuser
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)


admin.site.register(Election)
admin.site.register(ElectionInvite, ElectionInviteAdmin)
