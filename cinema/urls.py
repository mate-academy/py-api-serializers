from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    GenreViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
