from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyForm


def success_view(request):
    return render(request, 'NovaBazaar/success.html')

def signup(request):
    return render(request, 'NovaBazaar/signup.html')

def User(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
           
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            

            user_instance = User(first_name=first_name, email=email, password=password, confirm_password=confirm_password)
            user_instance.save()

            return redirect('success_page')
    else:
        form = MyForm()

    return render(request, 'NovaBazaar/index.html', {'form': form})

 

def Userlogin(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password = request.POST['Password']
        user = User.objects.filter(Email=Email, Password=Password)
        if user:
            return redirect('success')
        else:
            return HttpResponse('Invalid Credentials')
        
    return render(request, 'NovaBazaar/login.html')

