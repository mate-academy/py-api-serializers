# Generated by Django 4.0.4 on 2022-05-09 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cinema", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="moviesession",
            name="cinema_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cinema.cinemahall"
            ),
        ),
        migrations.AddField(
            model_name="moviesession",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cinema.movie"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(to="cinema.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="cinema.genre"),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("movie_session", "row", "seat")},
        ),
    ]
