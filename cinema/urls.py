from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("cinema/", include(router.urls)),
]
