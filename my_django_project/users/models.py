from django.db import models
from django.contrib.auth.models import User



class Booking(models.Model):
    VENUE_CHOICES = [
        ('venue1', 'Grand Ballroom'),
        ('venue2', 'Garden View Hall'),
        ('venue3', 'Beachfront Pavilion'),
    ]
    
    THEME_CHOICES = [
        ('theme1', 'Classic Elegance'),
        ('theme2', 'Rustic Charm'),
        ('theme3', 'Modern Chic'),
    ]
    
    FOOD_CHOICES = [
        ('veg', 'Veg'),
        ('non-veg', 'Non-veg'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    event_date = models.DateField()
    guests = models.PositiveIntegerField()
    
    venue = models.CharField(max_length=50, choices=VENUE_CHOICES)
    decoration_theme = models.CharField(max_length=50, choices=THEME_CHOICES)
    food_choice = models.CharField(max_length=50, choices=FOOD_CHOICES)

    def __str__(self):
        return f"{self.full_name} - {self.venue}"