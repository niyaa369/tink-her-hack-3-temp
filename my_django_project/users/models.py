from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Decoration(models.Model):
    name = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Catering(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('Veg', 'Vegetarian'), ('Non-Veg', 'Non-Vegetarian'), ('Both', 'Both')])

    def __str__(self):
        return self.name

class EventBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE)
    event_date = models.DateField()
    guests_count = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.username} - {self.event_date}"
