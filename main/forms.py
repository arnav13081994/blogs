from django import forms
from django.core.validators import MinLengthValidator



class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

