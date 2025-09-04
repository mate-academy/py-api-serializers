from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet, MovieViewSet,
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
