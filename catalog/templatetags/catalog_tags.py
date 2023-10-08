from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return f'/media/noimage.png'


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return f'/media/noimage.png'
