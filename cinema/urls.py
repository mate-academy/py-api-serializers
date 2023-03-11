from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
