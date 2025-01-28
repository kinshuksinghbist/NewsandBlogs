from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import NewsService

@login_required
def news_home(request):
    news_articles = NewsService.get_news_articles()
    return render(request, 'news/home.html', {'articles': news_articles})
