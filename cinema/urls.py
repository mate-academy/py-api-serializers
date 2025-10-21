from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
