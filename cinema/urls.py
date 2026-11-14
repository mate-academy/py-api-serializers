from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    GenreViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
