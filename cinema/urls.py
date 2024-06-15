from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("movies", MovieViewSet, basename="movies")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
