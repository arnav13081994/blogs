from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from main import models
from main import forms



# Create your views here.

def Signup(request):
    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm_Password']:
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            User.objects.create_user(username=name,
                                     email=email,
                                     password = password,
                                     first_name = name.split()[0]
                                     )  # Modify to set permissions according to chosen designation
            user_new = authenticate(username=name, password=password)   # It is because django by default will use username and password to authenticate
            login(request, user_new)
            messages.success(request, "You have signed up successfully, " + name.split()[0] + "!")
            return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "auth/components/signup.html", context)


def Login(request):
    form = forms.LoginForm()

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password, request=request)
            print(user)
            if user:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "auth/components/login.html", context)