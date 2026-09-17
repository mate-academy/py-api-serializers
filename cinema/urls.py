from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
