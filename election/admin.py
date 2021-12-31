from django.contrib import admin
from .models import Election, ElectionInvite, User


class ElectionAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = User.objects.filter(is_superuser=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ElectionInviteAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "sent_to":
            kwargs["queryset"] = User.objects.filter(is_superuser=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Election, ElectionAdmin)
admin.site.register(ElectionInvite, ElectionInviteAdmin)
