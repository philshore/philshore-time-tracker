from django.db import models
# Create your models here.


class TimeIn(models.Model):
    userId = models.IntegerField()
    dateIn = models.DateField('Date In', blank=True)
    timeIn = models.TimeField('time in', blank=True)


class TimeOut(models.Model):
    userId = models.IntegerField()
    dateOut = models.DateField('Date Out', blank=True)
    timeOut = models.TimeField('time out', blank=True)
