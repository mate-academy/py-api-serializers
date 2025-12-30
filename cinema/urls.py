from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet, ActorViewSet)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
