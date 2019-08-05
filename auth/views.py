from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from main import forms
from main import models

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode


keyy = b'''-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDlecLTo3GykOcUuuA/vah+EwO0gcP+COsJSnBnFpuG6sbo8yeg
4oiZleQ0OMjio+p9r1fc1fDlpjwhW6bexDJAEbKxkjjKwn41f/0jV028+QJ0rUSb
x0CP43fSE2zVGXOnM6vwTmzJOTvx6laTzw+fU0t5EWTZp3k762NpMGz3AQIDAQAB
AoGBAMTL43W1GfDVrBdvHJoNgM5+aBMJppfZ9heFq1f9X2wZNHTa8wVawWNV1Nuk
R0N258bZ9TQClhGcuryw6S7qe1wvFkh7bDSRBU1I3x0P0for800ud3VsXTnvDqMn
BxieO5yAWEmMc6hfV5pI30jSX0oGsWwjQi2kZAvTG15MrAkxAkEA8Qp6wojxFixS
mx9c3Unn8wB6mnG7t4x8uHJ/SpOSgjACFV+tApvz1mFIu/kCbgHqU7zrSkr4th/f
IhpltJojVwJBAPO3id2RIezqym8KPWrXtsnujMSDmnbZagAJ7D0PQ4zqI52OcfPY
5qT45cbICLVRR9+jmjyWS2L+X8KHjeCs2WcCQDbtImgt+HILC4/Zp7mtW7OeClIj
VJlQ5CLLxIHj+uC7u93O/Ye4renOJVrgNVOIEDOguyUkzGQEAz6sMTzkWuUCQQCi
/HdiiZCalFpU8BAqx6AiYzoYobpHCRbud7RZEUAnmN3AnGZwoPl+EkX4LgZE29qp
IQwgwJIh3ePEgErNmkq5AkB2er6lE0/Ca8zhVwJBByTE+R7Y0KGn4w+wa5RSE9bk
CYy1h2PPobHFY+gv6g9ITQaJtWx7yGI2ocNIHXue/O85
-----END RSA PRIVATE KEY-----'''


# Create your views here.

def Signup(request):
    form = forms.SignupForm()
    if request.method == "POST":
        key = RSA.importKey(keyy)
        cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            pass_1 = cipher.decrypt(b64decode(form.cleaned_data['password']))
            pass_conf = cipher.decrypt(b64decode(form.cleaned_data['confirm_Password']))
            if pass_1 == pass_conf:
                form.save()
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']

                user = User.objects.create_user(username=name,
                                         email=email,
                                         password = pass_1,
                                         first_name = name.split()[0]
                                         )  # Modify to set permissions according to chosen designation
                user_new = authenticate(username=name, password=pass_1)   # It is because django by default will use username and password to authenticate
                login(request, user_new)
                messages.success(request, "You have signed up successfully, " + name.split()[0] + "!")

                # Now add user to Author groups
                g = Group.objects.get(name='Author')
                g.user_set.add(user)

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
            key = RSA.importKey(keyy)
            cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
            password = cipher.decrypt(b64decode(password))
            user = authenticate(username=username, password=password, request=request)
            if user:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "auth/components/login.html", context)



def Reset(request):
    form = forms.ResetForm()

    if request.method == "POST":
        key = RSA.importKey(keyy)
        cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
        form = forms.ResetForm(request.POST)
        if form.is_valid():
            pass_1 = cipher.decrypt(b64decode(form.cleaned_data['new_password']))
            pass_conf = cipher.decrypt(b64decode(form.cleaned_data['confirm_new_password']))
            if pass_1 == pass_conf:
                email = form.cleaned_data['email']
                obj = models.Author.objects.get(email=email)
                name = obj.name
                user = User.objects.get(username=name)
                user.set_password(pass_1)
                user.save()
                user = authenticate(username=name, password=pass_1, request=request)
                if user:
                    login(request, user)
                    messages.success(request, "Password reset successfully!")
                    return HttpResponseRedirect('/')
    context = {
        'form': form
    }
    return render(request, "auth/components/reset.html", context)