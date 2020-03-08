from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:6]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })

        context = {
            'article_data': article_data,
        }

        return render(request, 'index.html', context)
