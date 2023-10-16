from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
