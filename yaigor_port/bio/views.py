from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Bio.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'bio/index.html', context=context)


def about(request):
    return render(request, 'bio/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Add post')


def contact(request):
    return HttpResponse('Contact with us')


def login(request):
    return HttpResponse('Sing in')


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1> Статьи по категориям<h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1> Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


