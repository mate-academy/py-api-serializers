from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions", MovieSessionViewSet, basename="moviesession")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
