from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()

router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"actors", ActorViewSet, basename="actors")

router.register(r"movies", MovieViewSet, basename="movies")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions",
)

urlpatterns = [
    path("api/cinema/", include(router.urls)),
]
