from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (CinemaHallViewSet,
                          MovieViewSet, GenreViewSet,
                          ActorViewSet, MovieSessionViewSet)

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet,
                basename="cinema_hall")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"movie_sessions", MovieSessionViewSet,
                basename="movie_sessions")

urlpatterns = [
    path("", include(router.urls)),
]
