from rest_framework.routers import DefaultRouter
from django.urls import path, include
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("cinema-halls", CinemaHallViewSet, basename="cinema-halls")
router.register("movies", MovieViewSet, basename="movies")
router.register("movie-sessions", MovieSessionViewSet, basename="movie-sessions")

urlpatterns = [
    path("", include(router.urls)),
]
