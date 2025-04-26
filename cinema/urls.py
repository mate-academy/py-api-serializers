from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
