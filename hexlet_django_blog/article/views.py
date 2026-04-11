from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        app_name = request.resolver_match.app_name
        context = {
            'app_name': app_name,
        }
        return render(
            request,
            'articles/index.html',
            context,
        )

# Create your views here.
