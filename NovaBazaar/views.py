from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyForm, Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.conf import settings




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
            print(request.POST)
            firstname = request.POST.get('FirstName')
            print("Firstname ", firstname)
            email = request.POST.get('Email', '')
            password = request.POST.get('Password', '')
            confirmPassword = request.POST.get('Confirm_password', '')
        
            user_instance = User(FirstName=firstname, Email=email, Password=password, confirm_password=confirmPassword)
            user_instance.save()
            
            return redirect('/success')
    else:
        form = MyForm()

    return render(request, 'NovaBazaar/index.html', {'form': form})
 

#def Userlogin(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            Password = request.POST.get('Password', '')
            
            user_instance = User(Email=email, Password=Password)
            user_instance.save()
            return redirect('/loginuser')
    else:
        form = Form()
    return render(request, 'NovaBazaar/login.html', {'form': form})
    
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
       
       
# def pass_reset_form(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             # Get the user associated with the provided email
#             email = form.cleaned_data['email']
#             user = User.objects.get(email=email)
            

#             # Create a PasswordResetView instance
#             reset_view = PasswordResetView.as_view()
  
#             # Use the PasswordResetView to send the reset email
#             reset_view(request)

#             return redirect('/password_reset_done')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'NovaBazaar/pass_reset_form.html', {'form': form})
def pass_reset_form(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            send_mail('Password reset', 'Here is the message.', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            
            # send_mail('Password reset', 'Here is the message.', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return render(request, 'NovaBazaar/password_reset_done.html')
    else:
        form = PasswordResetForm()
    return render(request, 'NovaBazaar/pass_reset_form.html', {'form': form})


def pass_reset_confirm(request):
    return render(request, 'NovaBazaar/pass_reset_confirm.html')

def pass_reset_done(request):
    return render(request, 'NovaBazaar/pass_reset_done.html')

def pass_reset_complete(request):
    return render(request, 'NovaBazaar/pass_reset_complete.html')

