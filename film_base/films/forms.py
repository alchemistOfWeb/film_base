from django import forms
from django.db.models.fields import SmallIntegerField
from .models import Film, Actor, Director, Genre, Review, Score
from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']


class RatingForm(forms.Form):
    rating = SmallIntegerField(max_length=5)
    film_id = forms.IntegerField()
    
    class Meta:
        model = Score
        fields = 'rating',


class FilmEditForm(forms.Form):
    actors = None
    directors = None


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
