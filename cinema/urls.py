# write urls here
from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions",
                MovieSessionViewSet,
                basename="movie_session")

urlpatterns = [path("", include(router.urls))]
