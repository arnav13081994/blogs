from django.shortcuts import render, get_object_or_404
from main import models


# Create your views here.
def Index(request):
    latest_articles = models.Article.objects.all().order_by('-created_at')[:10]
    context = {'latest_articles': latest_articles}
    return render(request, "main/index.html", context)


def Article(request, pk):

    article_info = get_object_or_404(models.Article, pk=pk)
    context = {
        'article_info': article_info,
    }

    return render(request, 'main/components/article.html', context)
