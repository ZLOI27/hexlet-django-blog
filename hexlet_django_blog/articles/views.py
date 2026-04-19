from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.articles.forms import ArticleForm

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
            'articles/create.html',
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
            'articles/create.html',
            context={'form': form}
        )


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'articles/update.html',
            context={'form': form, 'article_id': article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article_show', id=article.id)
        return render(
            request,
            'articles/update.html',
            context={'form': form, 'article_id': article_id}
        )


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs['id']
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
# Create your views here.
