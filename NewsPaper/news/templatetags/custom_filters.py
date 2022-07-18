
from django import template

register = template.Library()

@register.filter(name='censor')

def censor(value):

    black_list = ['nigger', 'подонок', 'засранец', 'Путин', 'fuck', 'Война', 'Радуга']

    for word in black_list:
        value = value.replace(word, '***')
    return value