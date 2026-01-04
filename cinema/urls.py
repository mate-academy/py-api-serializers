from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    GenreViewSet
)

router = DefaultRouter()
router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-hall"
)
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
