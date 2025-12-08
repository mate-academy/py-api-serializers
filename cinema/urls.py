from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorsViewSet,
    GenresViewSet,
    CinemaHallsViewSet,
    MoviesViewSet,
    MovieSessionsViewSet,
)

router = DefaultRouter()
router.register("actors", ActorsViewSet)

router.register("genres", GenresViewSet)

router.register("cinema_halls", CinemaHallsViewSet)

router.register("movies", MoviesViewSet)

router.register("movie_sessions", MovieSessionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
