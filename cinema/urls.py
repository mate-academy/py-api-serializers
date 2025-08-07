from rest_framework import routers
from django.urls import path, include
from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    GenreViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinemahall")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"genres", GenreViewSet, basename="genre")
router.register(
    r"movie_sessions",
    MovieSessionViewSet,
    basename="moviesession")
urlpatterns = [
    path("", include(router.urls)),
]


app_name = "cinema"
