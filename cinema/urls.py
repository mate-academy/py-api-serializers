from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorsViewSet,
    GenresViewSet,
    CinemaHallViewSet,
    MoviesViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()

router.register("actors", ActorsViewSet)
router.register("genres", GenresViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MoviesViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
