from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField(max_length=5000, verbose_name='description')
    poster = models.ImageField(upload_to='posters/%Y/%m/%d/')

    genres = models.ManyToManyField('Genre',
                                    verbose_name='genre',
                                    related_name='films', null=True)
    directors = models.ManyToManyField('Director',
                                       verbose_name='directors',
                                       related_name='films', null=True)
    actors = models.ManyToManyField('Actor',
                                    verbose_name='actors',
                                    related_name='films', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'film_pk': self.pk})

    def get_average_score(self):
        scores = self.scores.objects.all()

        return sum(map(lambda score: score.value, scores)) / len(scores)

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
    film = models.ForeignKey('Film', verbose_name='film', on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
