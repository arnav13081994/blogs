from django.shortcuts import render
from main import models


# Create your views here.
def Index(request):

    latest_articles = models.Article.objects.all().order_by('-created_at')[:10]

    context = {'latest_articles': latest_articles}

    return render(request, "main/index.html", context)


def Article(request, article_id):
    context= {'id': article_id}
    return render(request, 'main/components/article.html', context)
