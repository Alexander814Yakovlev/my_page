from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_list, name='todo-list'),
    path('<int:day>', views.get_todo_list_by_num),
    path('<str:day>', views.get_todo_list, name="todo-name"),
]
