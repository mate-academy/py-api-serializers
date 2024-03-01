from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    GenreViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
