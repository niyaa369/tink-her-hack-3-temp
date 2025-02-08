from django.urls import path
from .views import register, user_login, home

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
