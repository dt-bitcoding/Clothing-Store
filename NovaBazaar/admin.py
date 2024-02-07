from django.contrib import admin
from .models import Product, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'Email', 'Password', 'confirm_password')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'ProductName', 'Category', 'Order', 'Price')
    