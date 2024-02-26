from django.contrib import admin
from .models import Product, User, Category, Order, Cart, Customer
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib import admin
from django.contrib import admin
from .models import Cart

admin.site.register(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discount_price', 'description', 'brand', 'category', 'product_image')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total')

admin.site.register(Cart)
class CartAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'product', 'count')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'address', 'city', 'state', 'zipcode')