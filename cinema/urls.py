from django.urls import path, include

from rest_framework.routers import DefaultRouter
from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie-session"
)

urlpatterns = [
    path("cinema/", include(router.urls)),
]
