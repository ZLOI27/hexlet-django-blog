from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, tags='None', article_id=0, *args, **kwargs):
        app_name = request.resolver_match.app_name
        context = {
            'app_name': app_name,
            'tags': tags,
            'article_id': article_id,
        }
        return render(
            request,
            'articles/index.html',
            context,
        )


def index(request):
    return redirect('article', tags='python', article_id=42)
# Create your views here.
