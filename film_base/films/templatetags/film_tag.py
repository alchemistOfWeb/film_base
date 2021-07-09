from django import template
from films.models import Genre 
from django.conf import settings

register = template.Library()

@register.simple_tag()
def get_genres():
    return Genre.objects.all()
    
@register.simple_tag()
def get_user_film_score(film, user):
    result = film.get_score_of_user(user.id)
    return result

@register.filter(name='getattr')
def get_attr(item, attr):
    return getattr(item, attr)

# @register.filter(bane='get_score_by_film_id')
# def get_score_by_film_id(score_set, film_id):
#     return score_set.get(film_id=film_id)
