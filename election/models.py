from django.db import models
from authentication.models import User
from utilities.modelhelper import CommonFields, DateTracking


class ElectionType(models.TextChoices):
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTI_CHOICE = "MULTI_CHOICE"
    RANKED_CHOICE = "RANKED_CHOICE"
    INSTANT_RUNOFF = "INSTANT_RUNOFF"
    SINGLE_TRANSFER = "SINGLE_TRANSFER"


class ElectionResultType(models.TextChoices):
    CURRENT_RESULT = "CURRENT_RESULT"
    AFTER_VOTING = "AFTER_VOTING"
    AFTER_ELECTION = "AFTER_ELECTION"


class Election(DateTracking, CommonFields, models.Model):
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='election')
    election_type = models.CharField(
        max_length=15, choices=ElectionType.choices, default=ElectionType.SINGLE_CHOICE)
    result_type = models.CharField(
        max_length=14, choices=ElectionResultType.choices, default=ElectionResultType.CURRENT_RESULT)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ElectionInvite(DateTracking, models.Model):
    owned_by = models.ForeignKey(to=Election, on_delete=models.CASCADE)
    sent_to = models.ManyToManyField(User)
