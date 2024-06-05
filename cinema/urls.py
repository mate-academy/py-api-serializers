from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("movies", MovieViewSet, basename="movies")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = router.urls

app_name = "cinema"
