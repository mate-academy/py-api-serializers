# write urls here
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = DefaultRouter()
router.register("genres", GenreViewSet, "genre")
router.register("actors", ActorViewSet, "actor")
router.register("cinema_halls", CinemaHallViewSet, "cinema_hall")
router.register("movies", MovieViewSet, "movie")
router.register("movie_sessions", MovieSessionViewSet, "movie_session")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
