from __future__ import annotations
from typing import Any

from django.db import models


class Actor(models.Model):
    name: str = models.CharField(max_length=255, blank=True, null=True)
    first_name: str = models.CharField(max_length=100)
    last_name: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self) -> str:
        """Retorna o nome completo do ator (first_name + last_name)."""
        if self.name:
            return self.name
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name: str = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class CinemaHall(models.Model):
    name: str = models.CharField(max_length=255)
    rows: int = models.PositiveIntegerField()
    seats_in_row: int = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class Movie(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()
    duration: int = models.PositiveIntegerField()  # minutos
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title


class MovieSession(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="sessions")
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name="sessions")
    show_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.movie.title} @ {self.show_time.isoformat()}"
