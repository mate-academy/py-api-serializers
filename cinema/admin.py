from django.contrib import admin

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession

admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieSession)
