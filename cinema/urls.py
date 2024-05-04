from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls


app_name = "cinema"
