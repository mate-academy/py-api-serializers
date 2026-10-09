from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreView,
    ActorView,
    CinemaHallView,
    MovieView,
    MovieSessionView,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreView, basename="genre")
router.register("actors", ActorView, basename="actor")
router.register("cinema_halls", CinemaHallView, basename="cinemahall")
router.register("movies", MovieView, basename="movie")
router.register("movie_sessions", MovieSessionView, basename="moviesession")

urlpatterns = [
    path("", include(router.urls)),
]
