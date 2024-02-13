from django.db import models

# from django.contrib.auth.models import AbstractUser


class User(models.Model):
    FirstName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName

class Product(models.Model):
    Product = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Order = models.IntegerField()
    

    def __str__(self):
        return self.ProductName
    
    
