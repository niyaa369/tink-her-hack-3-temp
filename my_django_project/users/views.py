from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, BookingForm
from .models import Venue,Decoration,Catering

def register(request):
    print('heyyyyyy')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('home')  # Redirect to homepage
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def home(request):
    print('heyyyyy')
    return render(request, 'users/home.html')

# def book_event(request):
#     if request.method == 'POST':
#         form = EventBookingForm(request.POST)
#         if form.is_valid():
#             event_booking = form.save(commit=False)
#             event_booking.user = request.user  # Assign logged-in user
#             event_booking.save()
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         form = EventBookingForm()
    
#     venues = Venue.objects.all()
#     decorations = Decoration.objects.all()
#     caterings = Catering.objects.all()
    
#     return render(request, 'booknow.html', {
#         'form': form,
#         'venues': venues,
#         'decorations': decorations,
#         'caterings': caterings
#     })



def book_event(request):
    if request.method == "POST":
        print('tisejsfjnfjnrfj')
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print('sussecccc')
            return redirect('success_page')  # Redirect to a success page
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})


def success_page(request):
    return render(request, "success.html")
