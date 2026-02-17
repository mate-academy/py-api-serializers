from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
