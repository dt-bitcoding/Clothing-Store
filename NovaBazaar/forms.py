from django import forms

class MyForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

        
    
    