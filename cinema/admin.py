from django.contrib import admin
from .models import Genre, Actor, CinemaHall, Movie, MovieSession

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name')
    search_fields = ('first_name', 'last_name')

@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rows', 'seats_in_row', 'capacity')
    list_filter = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration')
    filter_horizontal = ('genres', 'actors')

@admin.register(MovieSession)
class MovieSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'cinema_hall', 'show_time')
    list_filter = ('movie', 'cinema_hall')
