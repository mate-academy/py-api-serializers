from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    ActorsViewSet,
    GenreViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorsViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
