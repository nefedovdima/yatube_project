from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со групп постов
    path('group_list/', views.group_posts),
]