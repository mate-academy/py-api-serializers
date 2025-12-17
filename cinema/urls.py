from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls)),
]
