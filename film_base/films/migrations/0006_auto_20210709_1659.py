# Generated by Django 3.2.4 on 2021-07-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imdb_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='kinopoisk_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='kinopoisk_rating',
            field=models.FloatField(null=True),
        ),
    ]
