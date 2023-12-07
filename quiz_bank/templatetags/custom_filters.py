from django import template

register = template.Library()

@register.filter
def letter(value):
    if value == 2:
        return 'A'
    elif value == 3:
        return 'B'
    elif value == 4:
        return 'C'
    elif value == 5:
        return 'D'
    else:
        return str(value)
