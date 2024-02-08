from django import forms

class MyForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
    
        
    
    