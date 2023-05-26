from django.urls import path, include
from rest_framework import routers

from .views import (
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    MovieViewSet,
    ActorViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)

urlpatterns = router.urls

app_name = "cinema"
