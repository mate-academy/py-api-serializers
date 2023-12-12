from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
