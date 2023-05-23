from django.urls import path, register_converter
from . import views, convertes

register_converter(convertes.YearConverter, 'yyyy')
register_converter(convertes.MyFloatConverter, 'float')
register_converter(convertes.MyDateConverter, 'date')
register_converter(convertes.SplitConvertor, 'my_list')
register_converter(convertes.UpperConvertor, 'caps')

urlpatterns = [
    path('', views.zodiac_list, name='horoscope-list'),
    path('type/', views.types, name='types-list'),
    path('type/<str:element>', views.elements, name='type-name'),
    path('<int:zodiac_sign>', views.get_zodiac_sign_info_by_number),
    path('<str:zodiac_sign>', views.get_zodiac_sign_info, name='horoscope-name'),
    path('<int:month>/<int:day>', views.get_zodiac_sign_by_date),
]
