from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
)

cinema_router = routers.DefaultRouter()
cinema_router.register("movies", MovieViewSet)
cinema_router.register("actors", ActorViewSet)
cinema_router.register("genres", GenreViewSet)
cinema_router.register("movie_sessions", MovieSessionViewSet)
cinema_router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("cinema/", include(cinema_router.urls)),
]

app_name = "cinema"
