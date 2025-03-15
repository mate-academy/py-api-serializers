from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    ActorSetView,
    GenreSetView,
    CinemaHallSetView,
    MovieSetView,
    MovieSessionSetView,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", ActorSetView, basename="actors")
router.register("genres", GenreSetView, basename="genres")
router.register("cinema_halls", CinemaHallSetView, basename="cinema-halls")
router.register("movies", MovieSetView, basename="movies")
router.register(
    "movie_sessions",
    MovieSessionSetView,
    basename="movie-sessions"
)

urlpatterns = [path("", include(router.urls))]
