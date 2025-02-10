from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions",
                MovieSessionViewSet,
                basename="movie-session"
                )


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
