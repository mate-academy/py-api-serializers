from django.contrib import admin

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket,
)

# admin.site.register(CinemaHall)
# admin.site.register(Genre)
# admin.site.register(Actor)
# admin.site.register(Movie)
# admin.site.register(MovieSession)
# admin.site.register(Order)
# admin.site.register(Ticket)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "full_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rows", "seats_in_row", "capacity"]
    search_fields = ["name"]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "duration"]
    filter_horizontal = ["genres", "actors"]
    search_fields = ["title"]


@admin.register(MovieSession)
class MovieSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "show_time", "movie", "cinema_hall"]
    list_filter = ["movie", "cinema_hall"]
    search_fields = ["movie__title"]
