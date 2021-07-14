from django import forms
from django.db.models.fields import SmallIntegerField
from django.forms import widgets
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


class AdminFilmForm(forms.ModelForm):
    
    # poster = forms.ImageField(required=False, widget=widgets.FileInput(attrs={}))
    description = forms.CharField(
                                  max_length=5000, 
                                  required=False, 
                                  widget=widgets.Textarea(attrs={'size': '8', 'cols': '130', 'rows': '20'})
                                  )

    imdb_id = forms.CharField(
                              label='imdb id', 
                              required=False, 
                              widget=widgets.TextInput(attrs={'class': 'vTextField', 'maxlength': '255'})
                              )

    kinopoisk_id = forms.CharField(
                                  label='kinopoisk id', 
                                  required=False, 
                                  widget=widgets.TextInput(attrs={'class': 'vTextField', 'maxlength': '255'})
                                  )

    

     # genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False)
     # directors = forms.ModelMultipleChoiceField(queryset=Director.objects.all(), required=False)
     # actors = forms.ModelMultipleChoiceField(queryset=Actor.objects.all(), required=False)

    
#     formfield_overrides = {
#         'imdb_id': {'required': False},
#         'kinopoisk_id': {'required': False},
#     }
    # use_required_attribute = False
    class Meta:
        
        model = Film
        fields = 'title', 'poster', 'description', 'imdb_id', 'kinopoisk_id', 'genres', 'directors', 'actors'


class CreateActorForm(forms.Form):
    ...


class CreateDirectorForm(forms.Form):
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
