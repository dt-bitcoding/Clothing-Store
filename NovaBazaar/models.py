from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .manager import UserManager


class User(AbstractUser):
    
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, blank=True, null=True)
    forgot_password = models.CharField(max_length=100, blank=True, null=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='Product/')

    def __str__(self):
        return self.title
    
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
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.FirstName + " " + self.product.name
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.FirstName
    
class Search(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    