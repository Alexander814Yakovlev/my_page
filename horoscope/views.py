from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


# Create your views here.
zodiac = {
        'aries': ["♈", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
        'taurus': ["♉", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
        'gemini': ["♊", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
        'cancer': ["♋", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
        'leo': ["♌", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
        'virgo': ["♍", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
        'libra': ["♎", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
        'scorpio': ["♏", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
        'sagittarius': ["♐", "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
        'capricorn': ["♑", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
        'aquarius': ["♒", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
        'pisces': ["♓", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
    }


def zodiac_list(request):
    """Страница со всеми знаками зодиака"""
    data = {
        'zodiac': zodiac,
    }
    return render(request, 'horoscope/zodiac_list.html', context=data)


def get_zodiac_sign_info(request, zodiac_sign: str):
    """Страница одного знака зодиака по имени"""
    data = {
        'sign': zodiac_sign,
        'description': zodiac[zodiac_sign],
    }
    return render(request, 'horoscope/info_zodiac.html', data)


def get_zodiac_sign_info_by_number(request, zodiac_sign: int):
    """Страница одного знака зодиака по номеру"""
    template = """
                <p style='font-size: 72px; text-align: center;'>
                    image
                </p><br>
                <p style='font-size: 30px; color:#a51fff; text-align: center;'>
                    content
                </p>"""

    if zodiac_sign in range(1, len(zodiac) + 1):
        zodiac_name = list(zodiac.keys())[zodiac_sign - 1]
        reverse_url = reverse('horoscope-name', args=(zodiac_name,))
        return HttpResponseRedirect(reverse_url)
    else:
        return HttpResponseNotFound(template.replace("image", "😵‍💫").replace("content", f"Знака зодиака {zodiac_sign} не существует.<br>Их всего 12!"))


def types(request):
    """Страница со всеми стихиями зодиака"""
    elements = {
        "fire": "🔥", "water": "💧",
        "air": "🌬️", "earth": "🌍",
    }
    data = {
        'elements': elements,
    }
    return render(request, 'horoscope/types_list.html', context=data)


def elements(request, element: str):
    """Страницы с знаками относящимися к стихии element"""
    elements = {
        "fire": ['aries', 'leo', 'sagittarius'],
        "water": ['cancer', 'scorpio', 'pisces'],
        "air": ['gemini', 'libra', 'aquarius'],
        "earth": ['taurus', 'virgo', 'capricorn'],
    }
    data = {
        'elements': elements,
        'element': element,
        'zodiac': zodiac,
    }
    return render(request, 'horoscope/info_element.html', context=data)


def get_zodiac_sign_by_date(request, month: int, day: int):
    days_count = {
        1: 31, 2: 29, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31,
    }

    if month not in days_count:
        return HttpResponseNotFound("Такого месяца не существует!")

    if day < 1 or day > days_count[month]:
        return HttpResponseNotFound(f"В {month}-м месяце всего {days_count[month]} дней!")

    # В переменной start будет номер дня, с которго в этом месяце начинается знак зодиака
    start = int(zodiac[list(zodiac)[month - 3]][1].split("(")[1].split()[1])
    # В переменной index будет номер знака зодиака, который передаётся в функцию get_zodiac_sign_info_by_number
    index = month - 2 if day >= start else month - 3
    # В моём случае функция get_zodiac_sign_info_by_number работает ТОЛЬКО с числами от 1 до 12
    # поэтому нужно дополнительно обработать месяцы с 1 по 3
    index = index if index > 3 else index + 12
    reverse_url = reverse('horoscope-name', args=[index])
    return HttpResponseRedirect(reverse_url)
