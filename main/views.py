from django.shortcuts import render
from Blog import Validators

# Create your views here.


def Index(request):

    context = {}
    return render(request, "main/index.html", context)


def Article(request, article_id):
    context= {'id': article_id}
    return render(request, 'main/article.html', context)


#@is_authenticated
#def Login(request):
#    context={}
#    return render(request, "main/login.html", context)