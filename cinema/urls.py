from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)

urlpatterns = [
    path("cinema/", include(router.urls))
]

app_name = "cinema"
