from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet
)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")

urlpatterns = [
    path("", include(router.urls))
]
