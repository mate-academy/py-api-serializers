from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie-list")
router.register("genres", GenreViewSet, basename="genre-list")
router.register("actors", ActorViewSet, basename="actor-list")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall-list")
router.register("movie_sessions", MovieSessionViewSet,
                basename="movie-session-list")

urlpatterns = [
    path("", include(router.urls)),
]
