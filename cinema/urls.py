from rest_framework import routers
from django.urls import path, include, reverse

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-session"
)

app_name = "cinema"


urlpatterns = [
    path("", include(router.urls))
]
