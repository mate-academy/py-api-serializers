from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema-halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
