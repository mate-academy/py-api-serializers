from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-session",
)
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    path("", include(router.urls)),
]
