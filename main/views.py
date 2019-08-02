from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import LoginView, LogoutView
from main import models
from main import forms


# Create your views here.


def Index(request):
    latest_articles = models.Article.objects.all().order_by('-created_at')[:10] # Get latest 10 articles
    context = {'latest_articles': latest_articles}
    return render(request, "main/index.html", context)

@login_required(login_url='/auth/login')  # This will make sure only autenticated users can read any article
def Article(request, pk):
    article_info = get_object_or_404(models.Article, pk=pk)
    context = {'article_info': article_info}
    return render(request, 'main/components/article.html', context)


def Signup(request):
    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm_Password']:
            author = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            User.objects.create_user(username=name,
                                     email=email,
                                     password = password,
                                     first_name = name.split()[0],
                                     last_name=name.split()[1]
                                     )  # Modify to set permissions according to chosen designation
            user_new = authenticate(username=name, password=password)   # It is because django by default will use username and password to authenticate
            login(request, user_new)
            messages.success(request, "You have signed up successfully, " + name.split()[0] + "!")
            return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "main/components/signup.html", context)



#class Login(LoginView):

#    template_name = "main/components/login.html"
#    redirect_authenticated_user = '/'
#
#

def Login(request):
    form = forms.LoginForm()

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password, request=request)
            print(user)
            if user:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "main/components/login.html", context)