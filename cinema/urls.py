from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("genres", GenreViewSet, basename="genres")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions"
)
router.register("actors", ActorViewSet, basename="actors")

urlpatterns = router.urls
