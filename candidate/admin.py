from django.contrib import admin
from .models import Candidate, CandidateGroup


class CandidateAdmin(admin.ModelAdmin):
    # TODO: Linked User, remove superuser

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateGroup)
