# write urls here
from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

router.register("movie_sessions", MovieSessionViewSet)

router.register("actors", ActorViewSet)

router.register("cinema_halls", CinemaHallViewSet)

router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "station"
