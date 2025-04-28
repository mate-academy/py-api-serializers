from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet, basename="movie")
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
urlpatterns = [
    path("", include(router.urls)),
]
