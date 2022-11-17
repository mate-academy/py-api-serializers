from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(
    r"movie_sessions",
    MovieSessionViewSet,
    basename="movie-session"
)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
