from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

cinema_router = routers.DefaultRouter()

cinema_router.register("genres", GenreViewSet, basename="genre")
cinema_router.register("actors", ActorViewSet, basename="actor")
cinema_router.register(
    "cinema_halls", CinemaHallViewSet, basename="cinema-hall"
)
cinema_router.register("movies", MovieViewSet, basename="movie")
cinema_router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie-session"
)

urlpatterns = [path("", include(cinema_router.urls))]
