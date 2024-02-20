from django import forms
from django.core.exceptions import ValidationError
from NovaBazaar.models import User
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

    # class Meta:
    #     model = User
    #     fields = ["email", "Password"]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get("email")
    #     password = cleaned_data.get("Password")
    #     user = authenticate(email=email, password=password)

    #     if password != user.password:
    #         raise forms.ValidationError("Passwords do not match")

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))