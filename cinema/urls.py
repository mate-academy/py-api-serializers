from django.urls import path, include
from rest_framework import routers
from rest_framework.urls import app_name

from cinema.views import (
    MovieSessionViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
