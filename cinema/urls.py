# write urls here
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions",
                MovieSessionViewSet,
                basename="movie_sessions"
                )

urlpatterns = [
    path("", include(router.urls)),
]
