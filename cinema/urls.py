from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieSessionViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet
)

app_name = "cinema"

router = DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
