from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Userform(UserCreationForm):
  
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

        
    
    