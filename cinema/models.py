from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self):
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name="sessions")
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, related_name="sessions"
    )

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return f"{self.movie.title} at {self.show_time}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="orders"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class Ticket(models.Model):
    movie_session = models.ForeignKey(
        MovieSession, on_delete=models.CASCADE,
        related_name="tickets"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="tickets")
    row = models.IntegerField()
    seat = models.IntegerField()

    class Meta:
        unique_together = ("movie_session", "row", "seat")

    def clean(self):
        if not (1 <= self.row <= self.movie_session.cinema_hall.rows):
            raise ValidationError({"row": "Invalid row number."})
        if not (1 <= self.seat <= self.movie_session.cinema_hall.seats_in_row):
            raise ValidationError({"seat": "Invalid seat number."})

    def __str__(self):
        return (
            f"Ticket for {self.movie_session} "
            f"(row: {self.row}, " f"seat: {self.seat})"
        )
