from django.contrib import admin

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)

admin.site.register(CinemaHall)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieSession)

