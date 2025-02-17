from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)


router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="cinema")
router.register("actors", ActorViewSet, basename="cinema")
router.register("genres", GenreViewSet, basename="cinema")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema")
router.register("movie_sessions", MovieSessionViewSet, basename="cinema")

urlpatterns = [
    path("cinema/", include(router.urls)),
]
app_name = "cinema"
