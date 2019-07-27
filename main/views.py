from django.shortcuts import render
from Blog import Validators
from main import models


# Create your views here.


def Index(request):

    latest_articles = models.Article.objects.all()[:6]

    # Get Article Imaage for Thumbnail

    article_images = []
    for i in latest_articles:
        article_images.append(i.thumbnail)




    # Get first 4 lines of every Article


    # Get the name of the author of that article


    # Get the time when the article was created



    context = {

        'latest_articles': latest_articles,
        'article_images': article_images,



               }

    return render(request, "main/index.html", context)


def Article(request, article_id):
    context= {'id': article_id}
    return render(request, 'main/components/article.html', context)











#@is_authenticated
#def Login(request):
#    context={}
#    return render(request, "main/login.html", context)