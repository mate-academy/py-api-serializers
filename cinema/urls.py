from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls))
]
