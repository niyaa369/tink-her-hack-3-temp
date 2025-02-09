from django.urls import path
from .views import register, user_login, home, book_event

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('book/', book_event, name='book_event'),
 path('success/', success_page, name='success_page')
]
