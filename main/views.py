from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from main import models
from main import forms


# Create your views here.


def Index(request):
    latest_articles = models.Article.objects.all().order_by('-created_at')[:10]
    context = {'latest_articles': latest_articles}
    return render(request, "main/index.html", context)


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
            messages.success(request, "You have signed up successfully, " + author.name.split()[0] + "!")
            return HttpResponseRedirect('/')

    context = {'form': form}
    return render(request, "main/components/signup.html", context)