from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieSessionViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()

router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
