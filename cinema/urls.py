from django.urls import path, include
from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)
from rest_framework import routers

app_name = "cinema"

router = routers.DefaultRouter()

router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema+hall")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)


urlpatterns = [
    path("", include(router.urls)),
]
