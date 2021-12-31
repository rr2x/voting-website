from django.contrib import admin
from .models import Candidate, CandidateGroup, User


class CandidateAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "linked_user":
            kwargs["queryset"] = User.objects.filter(is_superuser=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateGroup)
