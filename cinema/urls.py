from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinemaHalls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movieSessions", MovieSessionViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
