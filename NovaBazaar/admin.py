from django.contrib import admin
from .models import Product, User, Category, Order
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib import admin

admin.site.register(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total')

