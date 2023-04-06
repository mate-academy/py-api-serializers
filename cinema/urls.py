from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorView,
    GenreView,
    CinemaHallView,
    MovieView,
    MovieSessionView,
)

router = routers.DefaultRouter()
router.register("genres", GenreView, basename="genre")
router.register("actors", ActorView, basename="actor")
router.register("cinema_halls", CinemaHallView, basename="cinema_hall")
router.register("movies", MovieView, basename="movie")
router.register("movie_sessions", MovieSessionView, basename="movie_session")

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
