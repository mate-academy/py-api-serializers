from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    ActorViewSet,
    GenresViewSet,
    CinemaHallsViewSet,
    MoviesViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenresViewSet)
router.register("cinema_halls", CinemaHallsViewSet)
router.register("movies", MoviesViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
