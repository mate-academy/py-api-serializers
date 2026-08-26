from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()

router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie-sessions"
)

app_name = "cinema"

urlpatterns = [path("", include(router.urls))]
