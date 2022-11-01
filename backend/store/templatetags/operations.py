from django import template

register = template.Library()


@register.filter(name='money')
def money(number: int) -> str:
    return str(number) + "руб"


@register.filter(name='multiplay')
def multiplay(a: int, b: int) -> int:
    return a * b


@register.filter(name='summa')
def summa(a, b):
    return a + b
