from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def rectangle(request, width: int, height: int) -> HttpResponse:
    return render(request, 'geometry/rectangle.html')


def square(request, width: int) -> HttpResponse:
    return render(request, 'geometry/square.html')


def circle(request, radius: int) -> HttpResponse:
    return render(request, 'geometry/circle.html')


def get_rectangle_area(request, width: int, height: int) -> HttpResponse:
    reverse_url = reverse('rectangle-name', args=[width, height])
    return HttpResponseRedirect(reverse_url)


def get_square_area(request, width: int) -> HttpResponse:
    reverse_url = reverse('square-name', args=[width])
    return HttpResponseRedirect(reverse_url)


def get_circle_area(request, radius: int) -> HttpResponse:
    reverse_url = reverse('circle-name', args=[radius])
    return HttpResponseRedirect(reverse_url)