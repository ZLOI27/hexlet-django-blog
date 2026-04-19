from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'article/create.html',
            context={'form': form}
        )
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article_show', id=article.id)
        messages.error(request, 'error message')
        return render(
            request,
            'article/create.html',
            context={'form': form}
        )
# Create your views here.
