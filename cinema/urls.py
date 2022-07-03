from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieListViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieListViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
