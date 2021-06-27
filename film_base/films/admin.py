from django.contrib import admin
from .models import Film, Director, Actor, Genre, Review


# class FilmAdmin(admin.ModelAdmin):
#     list_display = 'id', 'title', 'description', 'poster'
#     list_display_links = 'id', 'title'
#     search_fields = 'title',


admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
