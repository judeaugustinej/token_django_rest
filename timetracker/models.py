from django.db import models
from django.conf import settings


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class TimeEntry(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
