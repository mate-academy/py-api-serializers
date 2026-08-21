from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet, MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"