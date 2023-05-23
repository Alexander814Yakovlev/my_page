from django import template
from translate import Translator

register = template.Library()


@register.filter(name='split')
def split_filter(value: str, key=' '):
    return value.split(key)


@register.filter(name="translate_ru")
def translate(value, to_lang="ru", from_lang='en'):
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    return translator.translate(value)
