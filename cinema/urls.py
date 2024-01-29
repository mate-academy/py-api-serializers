from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"actors", ActorViewSet, basename="actors")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register(r"movies", MovieViewSet, basename="movies")
router.register(
    r"movie_sessions", MovieSessionViewSet, basename="movie_sessions"
)


urlpatterns = [
    path("", include(router.urls))
]
