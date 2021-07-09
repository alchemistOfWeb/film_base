# Generated by Django 3.2.4 on 2021-07-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20210616_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='published_at'),
        ),
        migrations.AlterField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='films', to='films.Actor', verbose_name='actors'),
        ),
        migrations.AlterField(
            model_name='film',
            name='directors',
            field=models.ManyToManyField(related_name='films', to='films.Director', verbose_name='directors'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(related_name='films', to='films.Genre', verbose_name='genre'),
        ),
    ]
