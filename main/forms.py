from django import forms
from main import models


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    confirm_Password = forms.CharField(widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = models.Author
        fields = "__all__"
