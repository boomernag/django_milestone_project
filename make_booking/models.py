import uuid

from django.db import models
from django.conf import settings
from datetime import datetime


class timeslot(models.Model):
    timeslot_id = models.AutoField(primary_key=True)
    Date = models.DateField()
    TS1 = models.TextField(default = 'open')
    T2 = models.TextField(default = 'open')
    T3 = models.TextField(default = 'open')
    T4 = models.TextField(default = 'open')
    T5 = models.TextField(default = 'open')
    T6 = models.TextField(default = 'open')
    T7 = models.TextField(default = 'open')
    T8 = models.TextField(default = 'open')
    T9 = models.TextField(default = 'open')
    T10 = models.TextField(default = 'open')
    T11 = models.TextField(default = 'open')
    T12 = models.TextField(default = 'open')
    T13 = models.TextField(default = 'open')
    T14 = models.TextField(default = 'open')
    T15 = models.TextField(default = 'open')
    T16 = models.TextField(default = 'open')
    T17 = models.TextField(default = 'open')
    T18 = models.TextField(default = 'open')

    def __str__(self):
        return str(self.Date)
