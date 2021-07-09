import requests, json
from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


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
                                    verbose_name='genre',
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
        score = self.score_set.get(author_id=user_id)
        return score.value

    def get_stars_range(self):
        return range(self.STARS_NUMBER, 0, -1)

    def get_imdb_id(self):
        if not self.imdb_id:
            self.do_save = True

            request_film = requests.get(f'https://imdb-api.com/{self.LANG}/API/SearchMovie/{settings.IMDB_API_KEY}/{self.title}')

            if request_film.status_code != 200 :
                return ''

            film_data = json.loads(request_film.text)

            if film_data['errorMessage'] != '':
                return ''
            
            imdb_film_id = film_data['results'][0]['id']
            self.imdb_id = imdb_film_id
        
        return self.imdb_id

    def get_imdb_rating(self):
        if not self.get_imdb_id():
            return ''

        if not self.imdb_rating:
            self.do_save = True
            request_film_rating = requests.get(f'https://imdb-api.com/{self.LANG}/API/Ratings/{settings.IMDB_API_KEY}/{self.imdb_id}')

            ratings_data = json.loads(request_film_rating.text)
            if request_film_rating.status_code != 200 or ratings_data['error_message'] != '':
                return ''

            imdb_film_rating = ratings_data['imDb']
            self.imdb_rating = imdb_film_rating
        
        if self.do_save:
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
