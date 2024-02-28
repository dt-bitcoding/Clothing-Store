from django import template

register = template.Library()

@register.filter(name='is_numeric')
def is_numeric(value):
    return value.isdigit()