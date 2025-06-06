from django.urls import path
from rest_framework import routers

from .views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)
router.register("cinema-halls", CinemaHallViewSet)

app_name = "cinema"

urlpatterns = router.urls
