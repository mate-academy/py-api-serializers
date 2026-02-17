from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet
)

router = DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register(
    "movies",
    MovieViewSet,
    basename="movies"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = [
    path("", include(router.urls)),
]
