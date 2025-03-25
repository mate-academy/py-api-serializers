from django.urls import include, path
from rest_framework import routers

from cinema.views import (ActorViewSet,
                          CinemaHallViewSet,
                          GenreViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("movies", MovieViewSet, basename="movies")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = [
    path("", include(router.urls)),
]
