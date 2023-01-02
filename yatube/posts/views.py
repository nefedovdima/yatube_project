from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком посты
def group_posts(request, slug):
    return HttpResponse(f'Пост {slug}')
