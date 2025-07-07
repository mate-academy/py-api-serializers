from django.urls import path, include
from rest_framework import routers

from .views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls)),
]
