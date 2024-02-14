from django.contrib import admin
from .models import Product, User, Category, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'Email', 'Password', 'confirm_password')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total')


