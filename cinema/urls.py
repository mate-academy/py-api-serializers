from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions")

urlpatterns = [
    path("", include(router.urls)),
]
