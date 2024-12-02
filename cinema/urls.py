from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("api/cinema/", include(router.urls)),
]
