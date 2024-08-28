from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-halls"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions"
)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
