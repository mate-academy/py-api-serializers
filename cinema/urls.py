from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls"),
router.register("movies", MovieViewSet, basename="movies"),
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions"
)

urlpatterns = [
    path("", include(router.urls))
]
