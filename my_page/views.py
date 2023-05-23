from django.shortcuts import render
from django.urls import reverse


def main_page(request):
    data = {
        "horoscope_url": reverse('horoscope-list'),
        "todo_url": reverse('todo-list'),
    }
    return render(request, 'horoscope/index.html', data)
