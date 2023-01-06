from django.urls import path
from . import views

# Эта строчка обязательна. 
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со групп постов
    path('group_list/', views.group_posts, name='group_posts'),
]