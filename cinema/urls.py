from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("movies", MovieViewSet, basename="movies")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
