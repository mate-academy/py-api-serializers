from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieSessionViewSet,
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
