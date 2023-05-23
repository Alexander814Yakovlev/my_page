from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
days = {
    'monday': 'понедельник',
    'tuesday': 'вторник',
    'wednesday': 'среду',
    'thursday': 'четверг',
    'friday': 'пятницу',
    'saturday': 'субботу',
    'sunday': 'воскресенье'
    }


def days_list(request) -> HttpResponse:
    links = "".join([f"<a href='{k}' style='font-size: 40px; text-decoration: none;'>{v[:-1] + 'а' if v.endswith('у') else v}</a>" for k, v in days.items()])
    template = f"""
    <body>
        <div style='display: flex; flex-wrap: wrap; justify-content: space-around; align-items: center; height: -webkit-fill-available;'>
            {links}
        </div>
    </body>
    """
    return HttpResponse(template)


def get_todo_list(request, day: str) -> HttpResponse|HttpResponseNotFound:
    if day == "monday":
        return render(request, 'week_days/greeting.html')
    elif day in days:
        return HttpResponse(f"""
        <p style='font-size: 32px; text-align: center;'>Список дел на {days[day]}</p>
        <ul style='text-align: center; font-size:50px;'>
            <li>Work it</li>
            <li>Make it</li>
            <li>Do it</li>
            <li>Makes us</li>
            <li>Harder</li>
            <li>Better</li>
            <li>Faster</li>
            <li>Stronger</li>
        </ul>
        """)
    else:
        return HttpResponseNotFound("""
        <p style='font-size: 32px; text-align: center;'>Такого дня недели не бывает:)</p>
        """)


def get_todo_list_by_num(request, day: int) -> HttpResponseRedirect|HttpResponseNotFound:
    if day in range(1, len(days) + 1):
        day_name = list(days)[day - 1]
        reverse_url = reverse('todo-name', args=[day_name])
        return HttpResponseRedirect(reverse_url)
    else:
        return HttpResponseNotFound(f"""
        <p style='font-size: 32px; text-align: center;'>Дня недели с номером {day} не бывает:)<br>Их всего семь!</p>
        """)