from django.db import models
from authentication.models import User
from utilities.modelhelper import CommonFields, DateTracking
from election.models import Election


class CandidateGroup(DateTracking, CommonFields, models.Model):

    def __str__(self):
        return self.name


class Candidate(DateTracking, CommonFields, models.Model):
    owned_by_election = models.ForeignKey(
        to=Election, on_delete=models.CASCADE)
    linked_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    candidate_group = models.ForeignKey(
        null=True, blank=True, to=CandidateGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
