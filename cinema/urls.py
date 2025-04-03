from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
