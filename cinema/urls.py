from django.urls import path, include
from rest_framework import routers

from .views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = routers.DefaultRouter()

router.register("actors", ActorViewSet)
router.register("cinema-halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)


urlpatterns = [path("", include(router.urls))]


app_name = "cinema"
