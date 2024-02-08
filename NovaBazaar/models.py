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
    ProductName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Order = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ProductName
    
    
