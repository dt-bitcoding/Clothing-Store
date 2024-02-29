from django import forms

from django.core.exceptions import ValidationError
from NovaBazaar.models import User, Product, Customer, Cart, Order
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class MyForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["FirstName", "Email", "Password", "confirm_password"]

    def clean(self):

        cleaned_data = super().clean()
        password = cleaned_data.get("Password")
        confirm_password = cleaned_data.get("Confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class Form(forms.Form):
    email = forms.EmailField(max_length=100)
    Password = forms.CharField(max_length=100)

class Cart(forms.Form):
    model = Cart
    fields = ["user", "product"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "selling_price", "discount_price", "description", "brand", "category", "product_image"]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "address", "city", "state", "zipcode"]
        
class BuyNowForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["user", "customer", "product", "quantity", "price", "address", "phone", "date"]
    
    