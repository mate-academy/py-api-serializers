from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    CinemaHallViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = router.urls
