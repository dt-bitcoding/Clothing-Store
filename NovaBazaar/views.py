from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyForm, Form


def success_view(request):
    return render(request, 'NovaBazaar/success.html')

def signup(request):
    return render(request, 'NovaBazaar/signup.html')

def user(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            Firstname = request.POST.get('Firstname', '')
            Email = request.POST.get('Email', '')
            Password = request.POST.get('Password', '')
            Confirm_password = request.POST.get('Confirm_password', '')
        
            user_instance = User(FirstName=Firstname, Email=Email, Password=Password, confirm_password=Confirm_password)
            user_instance.save()
            
            return redirect('/success')
    else:
        form = MyForm()

    return render(request, 'NovaBazaar/index.html', {'form': form})
 

def Userlogin(request):
    
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():

            Email = request.POST.get('Email', '')
            Password = request.POST.get('Password', '')
            
            user_instance = User(Email=Email, Password=Password)
            user_instance.save()
            
            return redirect('/loginuser')
    else:
        form = Form()

    return render(request, 'NovaBazaar/login.html', {'form': form})
