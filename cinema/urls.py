from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions", MovieSessionViewSet, basename="moviesession")

urlpatterns = [
    path("cinema/", include(router.urls)),
]
