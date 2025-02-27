from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-hall",
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions",
)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
