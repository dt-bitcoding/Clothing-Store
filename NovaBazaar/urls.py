from django.urls import path
from . import views

# app_name = 'home'  # Add this line to set the app namespace

urlpatterns = [
    path('', views.User, name='index'),
   
]

