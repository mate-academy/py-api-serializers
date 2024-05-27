from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

router = DefaultRouter()
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("movie_sessions",
                MovieSessionViewSet,
                basename="movie_sessions")

urlpatterns = [
    path("", include(router.urls))
]
