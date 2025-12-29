from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie_session"
)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
