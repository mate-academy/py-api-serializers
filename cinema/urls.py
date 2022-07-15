from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieSessionViewSet,
    MovieViewSet,
    GenreViewSet,
    ActorViewSet
)

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
