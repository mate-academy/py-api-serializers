from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet
)
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
urlpatterns = [
    path("", include(router.urls))
]
