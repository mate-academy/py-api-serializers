from django.contrib import admin
from .models import (Genre,
                     Actor,
                     Movie,
                     CinemaHall,
                     MovieSession,
                     Order,
                     Ticket)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "duration"]
    filter_horizontal = ["genres", "actors"]


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rows", "seats_in_row", "capacity"]


@admin.register(MovieSession)
class MovieSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "movie", "cinema_hall", "show_time"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "movie_session", "order", "row", "seat"]
