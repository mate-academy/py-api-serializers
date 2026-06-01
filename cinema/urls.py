from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()

router.register("cinema/cinema_halls", CinemaHallViewSet)
router.register("cinema/actors", ActorViewSet)
router.register("cinema/genres", GenreViewSet)
router.register("cinema/movies", MovieViewSet)
router.register("cinema/movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
