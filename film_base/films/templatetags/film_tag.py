from django import template
from films.models import Genre 


register = template.Library()

@register.simple_tag()
def get_genres():
    return Genre.objects.all()

@register.filter(name='getattr')
def get_attr(item, attr):
    return getattr(item, attr)
