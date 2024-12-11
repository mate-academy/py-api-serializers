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
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
