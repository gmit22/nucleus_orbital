from django.db import models
import datetime
# Create your models here.
class Sport(models.Model):

    sport = models.CharField(max_length=100)
    location = models.TextField()
    Timing = models.TextField()

    def __str__(self):
        return self.sport

class Booking(models.Model):

    dt = models.DateField('date', default=datetime.date.today, unique=True)
    lt = models.TextField()
    st = models.TextField(default='free')
    peer = models.TextField(default='no')


    def __str__(self):
        return str(self.dt)












