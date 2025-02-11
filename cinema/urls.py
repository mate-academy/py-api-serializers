from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
