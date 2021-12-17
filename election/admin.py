from django.contrib import admin
from .models import Election, ElectionInvite, Candidate, CandidateGroup

# temporary registration test
admin.site.register(Election)
admin.site.register(ElectionInvite)
admin.site.register(Candidate)
admin.site.register(CandidateGroup)
