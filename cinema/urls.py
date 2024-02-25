from rest_framework import routers
from .views import (
    MovieViewSet, MovieSessionViewSet, CinemaHallViewSet,
    GenreViewSet, ActorViewSet
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
