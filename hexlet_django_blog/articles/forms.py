from django.forms import ModelForm
from hexlet_django_blog.articles.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']