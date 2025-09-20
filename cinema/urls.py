from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorsViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)
from rest_framework import routers

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorsViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie_session"
)

urlpatterns = [
    path("", include(router.urls)),
]
