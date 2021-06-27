from django import forms
from .models import Film, Actor, Director, Genre, Review


class ActorForm(forms.Form):
    ...


class DirectorForm(forms.Form):
    ...


class GenreForm(forms.Form):
    ...


class FilmForm(forms.Form):
    ...


class ReviewForm(forms.Form):
    ...

    class Meta:
        model = Review
        fields = 'text',
