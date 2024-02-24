from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
