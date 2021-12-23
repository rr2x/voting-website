from django.contrib import admin
from .models import Candidate, CandidateGroup

admin.site.register(Candidate)
admin.site.register(CandidateGroup)
