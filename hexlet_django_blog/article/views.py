from django.shortcuts import render
from django.http import HttpResponse


def index(request):
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
