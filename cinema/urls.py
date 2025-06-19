from django.urls import path, include
from rest_framework import routers
from .views import (
    GenreViewSet, ActorViewSet, CinemaHallViewSet,
    MovieViewSet, MovieSessionViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet,
                basename="genre")
router.register(r"actors", ActorViewSet,
                basename="actor")
router.register(r"cinema_halls", CinemaHallViewSet,
                basename="cinema_hall")
router.register(r"movies", MovieViewSet,
                basename="movie")
router.register(r"movie_sessions", MovieSessionViewSet,
                basename="movie_session")

urlpatterns = [
    path("", include(router.urls)),
]
