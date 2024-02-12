from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallSet)
router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
