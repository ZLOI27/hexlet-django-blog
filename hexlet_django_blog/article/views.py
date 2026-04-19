from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.article.models import Article

class IndexView(View):
    def get(self, request, article_id=0, *args, **kwargs):
        articles = Article.objects.all()[:15]
        context = {
            "articles": articles,
        }
        return render(
            request,
            'articles/articles_list.html',
            context,
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={
                'article': article
            }
        )
# Create your views here.
