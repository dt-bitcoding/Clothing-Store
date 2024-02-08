from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import MyForm


def success_view(request):
    return render(request, 'NovaBazaar/success.html')

def signup(request):
    return render(request, 'NovaBazaar/signup.html')

def user(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            First_name = request.POST.get('First_name', '')
            Email = request.POST.get('Email', '')
            Password = request.POST.get('Password', '')
            Confirm_password = request.POST.get('Confirm_password', '')
        
            user_instance = User(FirstName=First_name, Email=Email, Password=Password, confirm_password=Confirm_password)
            user_instance.save()
            
            return redirect('/success')
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
