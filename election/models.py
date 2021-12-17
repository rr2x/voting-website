from django.db import models
from authentication.models import User
from utilities.modelhelper import CommonFields, DateTracking


class Election(DateTracking, CommonFields, models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='election')
