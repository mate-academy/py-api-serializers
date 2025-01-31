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


class MovieSessionInLine(admin.TabularInline):
    model = MovieSession
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = (MovieSessionInLine,)


admin.site.register(MovieSession)
admin.site.register(Movie, MovieAdmin)
admin.site.register(CinemaHall)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Order)
admin.site.register(Ticket)
