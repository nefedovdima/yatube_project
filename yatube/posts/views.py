from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render

# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template) 


# Страница со списком посты
def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)