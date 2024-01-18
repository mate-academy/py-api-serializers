from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
