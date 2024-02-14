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
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return self.user.FirstName + " " + self.product.name
    