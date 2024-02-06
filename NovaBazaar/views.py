from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def User(request):
    return render(request, 'NovaBazaar/index.html')


