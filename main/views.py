from django.shortcuts import render
from main import models


# Create your views here.
def Index(request):
    latest_articles = models.Article.objects.all().order_by('-created_at')[:10]
    context = {'latest_articles': latest_articles}
    return render(request, "main/index.html", context)


def Article(request, pk):

    article_info = models.Article.objects.get(id=pk)
    author_list = article_info.authors.all() # get list of all articles for the given article
    context = {
        'article_info': article_info,
        'author_list': author_list
    }

    return render(request, 'main/components/article.html', context)
