from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render





# Главная страница
def index(request):
    context = {
    'title' : 'Это главная страница проекта Yatube',
    }
    template = 'posts/index.html'
    return render(request, template, context) 


# Страница со списком посты
def group_posts(request):
    context = {
    'title' : 'Здесь будет информация о группах проекта Yatube'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)