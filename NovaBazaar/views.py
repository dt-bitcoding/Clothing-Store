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
            
            # first_name = form.cleaned_data['First_name']
            # print("Hello Data.....")
            # email = form.cleaned_data['Email']
            # password = form.cleaned_data['Password']
            # confirm_password = form.cleaned_data['Confirm_password']
               
            First_name = request.POST.get('First_name', '')
            Email = request.POST.get('Email', '')
            Password = request.POST.get('Password', '')
            Confirm_password = request.POST.get('Confirm_password', '')
            

            # user_instance = User(FirstName=first_name, Email=email, Password=password, Confirm_password=confirm_password)
            # user_instance = User(first_name=FirstName, email=Email, password=Password, confirm_password=Confirm_password)
           

            # user_instance = User(firstName=first_name, email=email, password=password, confirm_password=confirm_password)
            user_instance = User(FirstName=First_name, Email=Email, Password=Password, confirm_password=Confirm_password)
            print("Hello Data.....")
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

