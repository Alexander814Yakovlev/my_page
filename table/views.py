from django.shortcuts import render

# Create your views here.


def get_table(request):
    return render(request, 'table/beautiful_table.html')
