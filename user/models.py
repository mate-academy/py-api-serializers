from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def __str__(self):
        return self.full_name


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def capacity(self):
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="get_movies")

    def __str__(self):
        return self.title


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(
        Movie,
        related_name="movie_sessions",
        on_delete=models.CASCADE
    )
    cinema_hall = models.ForeignKey(
        CinemaHall,
        related_name="movie_sessions",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (f"{self.movie.title}"
                f" at {self.show_time}"
                f" in {self.cinema_hall.name}")


class User(AbstractUser):
    pass
