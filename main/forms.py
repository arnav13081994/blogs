from django import forms
from main import models

class SignupForm(forms.ModelForm):
    EXPERIENCE = (
        (1, '< 1 year'),
        (2, '1-2 years'),
        (3, '2-5 years'),
        (4, '5+ years'),
    )
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    confirm_Password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    experience = forms.ChoiceField(choices= EXPERIENCE)
    reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Why do you want to join us?'}))

    class Meta:
        model = models.Author
        fields = ("name", "email")


# TODO Need to create an Article Create and update and Delete view

class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = models.Author
        fields = ('name',)




class ResetForm(forms.ModelForm):
    email = forms.EmailField()
    new_password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = models.Author
        exclude = ('email', 'name', 'user')

