from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    GenresViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenresViewSet)

urlpatterns = [path("", include(router.urls))]
