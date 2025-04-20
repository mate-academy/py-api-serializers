# write urls here
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
