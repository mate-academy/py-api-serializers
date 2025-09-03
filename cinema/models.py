from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-show_time"]

    def __str__(self) -> str:
        return f"{self.movie.title} ({self.show_time})"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Order {self.id} by {self.user} at {self.created_at}"


class Ticket(models.Model):
    movie_session = models.ForeignKey(
        MovieSession, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    def clean(self) -> None:
        cinema_hall = self.movie_session.cinema_hall

        if not (1 <= self.row <= cinema_hall.rows):
            raise ValidationError(
                {"row": f"Row number must be in range 1 to {cinema_hall.rows}"}
            )

        if not (1 <= self.seat <= cinema_hall.seats_in_row):
            raise ValidationError(
                {
                    "seat": (
                        f"Seat number must be in range 1 to "
                        f"{cinema_hall.seats_in_row}"
                    )
                }
            )

    def __str__(self) -> str:
        return f"{self.movie_session} (row: {self.row}, seat: {self.seat})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie_session", "row", "seat"],
                name="unique_ticket_per_seat",
            )
        ]
