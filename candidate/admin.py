from django.contrib import admin
from election.models import Candidate, CandidateGroup

admin.site.register(Candidate)
admin.site.register(CandidateGroup)
