from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyForm, Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
 

def success_view(request):
    return render(request, 'NovaBazaar/success.html')

def signup(request):
    return render(request, 'NovaBazaar/signup.html')

def logout(request):
    return render(request, 'NovaBazaar/index.html')

def user(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            firstname = request.POST.get('Firstname', '')
            email = request.POST.get('Email', '')
            password = request.POST.get('Password', '')
            confirmPassword = request.POST.get('Confirm_password', '')
        
            user_instance = User(FirstName=firstname, Email=email, Password=password, confirm_password=confirmPassword)
            user_instance.save()
            
            return redirect('/success')
    else:
        form = MyForm()

    return render(request, 'NovaBazaar/index.html', {'form': form})
 

# def Userlogin(request):
#     if request.method == 'POST':
#         form = Form(request.POST)
#         if form.is_valid():
#             email = request.POST.get('email', '')
#             Password = request.POST.get('Password', '')
            
#             user_instance = User(Email=email, Password=Password)
#             user_instance.save()
#             return redirect('/loginuser')
#     else:
#         form = Form()
#     return render(request, 'NovaBazaar/login.html', {'form': form})
    
def Userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            Password = request.POST.get('Password', '')
            user = authenticate(request, Email=email, Password=Password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  # Redirect to the home page after successful login
    else:
        form = Form()
    return render(request, 'NovaBazaar/login.html', {'form': form})
            