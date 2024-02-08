from django import forms

class MyForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(max_length=100)
    Confirm_password = forms.CharField(max_length=100)


class Form(forms.Form):
    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(max_length=100)
