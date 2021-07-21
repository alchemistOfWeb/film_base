from .exceptions import IMDBConnectionError, IMDBException
import requests, json
from django.db import models
from django.core import validators
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from .functions import get_imdb_id, get_imdb_rating

class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField(max_length=5000, verbose_name='description')
    poster = models.ImageField(upload_to='posters/%Y/%m/%d/')

    imdb_id = models.CharField(max_length=255, null=True)
    imdb_rating = models.FloatField(null=True)

    kinopoisk_id = models.CharField(max_length=255, null=True)
    kinopoisk_rating = models.FloatField(null=True)

    STARS_NUMBER = 5
    LANG='en'

    genres = models.ManyToManyField('Genre',
                                    verbose_name='genres',
                                    related_name='films')
    directors = models.ManyToManyField('Director',
                                    verbose_name='directors',
                                    related_name='films')
    actors = models.ManyToManyField('Actor',
                                    verbose_name='actors',
                                    related_name='films')

            
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'film_pk': self.pk})

    def get_average_score(self):
        scores = self.score_set.all()
        result = 0

        if scores:
            result = sum(map(lambda score: score.value, scores)) / len(scores)

        return result

    def get_score_of_user(self, user_id):
        try:
            score = self.score_set.get(author_id=user_id)
        except ObjectDoesNotExist:
            return 0

        return score.value

    def get_stars_range(self):
        return range(self.STARS_NUMBER, 0, -1)

    def get_imdb_rating(self):
        do_save = False

        try:
            if not self.imdb_id:
                self.imdb_id = get_imdb_id(self.title, settings.IMDB_API_KEY, lang=settings.API_LANG)
                do_save = True

            if not self.imdb_rating:
                self.imdb_rating = get_imdb_rating(self.imdb_id, settings.IMDB_API_KEY, lang=settings.API_LANG)
                do_save = True
        except IMDBException as e:
            if settings.DEBUG:
                print('IMDBException ERROR: ', e.message)
                raise IMDBException(e.message)

            return ''
        except IMDBConnectionError as e:
            if settings.DEBUG:
                print('IMDBException ERROR: {e.message} Status code: {e.status_code}')
                raise IMDBConnectionError(e.message, e.status_code)

            return ''
        
        if do_save:
            self.save()

        return self.imdb_rating


    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class Actor(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'


class Score(models.Model):
    value = models.PositiveSmallIntegerField(validators=[validators.MaxValueValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey('Film', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.value) + 'points'

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'


class Review(models.Model):
    text = models.TextField('text', max_length=5000)
    published_at = models.DateTimeField(
                                        verbose_name='published_at', 
                                        auto_now_add=True, 
                                        db_index=True, 
                                        null=True)
                                        
    film = models.ForeignKey('Film', verbose_name='film', on_delete=models.CASCADE,
                             null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
