from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    GenreViewSet,
    CinemaHallsViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet, basename="actors")
router.register("movies", MovieViewSet, basename="movies")
router.register("genres", GenreViewSet, basename="genres")
router.register("cinema_halls", CinemaHallsViewSet, basename="cinema_halls")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
