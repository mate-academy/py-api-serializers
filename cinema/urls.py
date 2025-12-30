from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieSessionViewSet, MovieViewSet, ActorViewSet,
    CinemaHallViewSet, GenreViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
