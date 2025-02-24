from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, какой это прекрасный магазин и почему нужно покупать именно мебель именно здесь'
    }

    return render(request, 'main/about.html', context)
