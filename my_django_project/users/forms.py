from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




# class EventBookingForm(forms.ModelForm):
#     class Meta:
#         model = EventBooking
#         fields = ['venue', 'decoration', 'catering', 'event_date', 'guests_count']




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'event_date', 'guests', 'venue', 'decoration_theme', 'food_choice']