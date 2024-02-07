from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def User(request):
    if request.method == 'POST':
        print("Hello Data...!!")
        FirstName = request.POST['FirstName']
        Email = request.POST['Email']
        Password = request.POST['Password']
        confirm_password = request.POST['confirm_password']
        user = User(FirstName=FirstName, Email=Email, Password=Password, confirm_password=confirm_password)
        user.save()
        # return redirect('success')
        return HttpResponse('User created successfully')
    else:
        return render(request, 'NovaBazaar/index.html')
    

        

    


def success_view(request):
    return render(request, 'NovaBazaar/success.html')


        


