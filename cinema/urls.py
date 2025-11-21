# write urls here
from rest_framework import routers
from django.urls import path, include
from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_sessions")
router.register("Actors", ActorViewSet, basename="actors")
router.register("Genres", GenreViewSet, basename="genres")
router.register("CinemaHall", CinemaHallViewSet, basename="cinemaHalls")

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
