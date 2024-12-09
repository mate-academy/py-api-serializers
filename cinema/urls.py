from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
