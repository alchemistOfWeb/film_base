# Generated by Django 3.2.4 on 2021-06-14 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(null=True, to='films.Actor', verbose_name='актёры'),
        ),
        migrations.AlterField(
            model_name='film',
            name='directors',
            field=models.ManyToManyField(null=True, to='films.Director', verbose_name='режисёры'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(null=True, to='films.Genre', verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='film',
            name='scores',
            field=models.ManyToManyField(null=True, to='films.Score', verbose_name='оценки'),
        ),
    ]