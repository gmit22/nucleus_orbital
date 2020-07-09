from django.db import models

# Create your models here.
class BookingManager(models.Model):

    userid = models.CharField(max_length=100)
    upcoming_bookings = models.TextField()
    past_bookings = models.TextField()

    def __str__(self):
        return self.userid
