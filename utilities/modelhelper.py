from django.db import models


class DateTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonFields(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True
