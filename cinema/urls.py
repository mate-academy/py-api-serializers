from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("movie", MovieViewSet)
router.register("movie_session", MovieSessionViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
