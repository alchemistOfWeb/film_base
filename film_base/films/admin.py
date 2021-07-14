from typing import Optional
from django.contrib import admin
from .models import Film, Director, Actor, Genre, Review
from .forms import AdminFilmForm


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    
    list_display = 'title', 'poster', 'imdb_rating', 'kinopoisk_rating'
    list_display_links = 'title',
    search_fields = 'title',

    # list_select_related = True
    fields = 'title', 'poster', 'description', ('imdb_id', 'kinopoisk_id'), 'genres', 'directors', 'actors'
    exclude = 'imdb_rating', 'kinopoisk_rating'

    # def get_form(self, request, obj, change, **kwargs):
    #     print(kwargs)

    #     return super().get_form(request, obj=obj, change=change, **kwargs)

    form = AdminFilmForm


admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
