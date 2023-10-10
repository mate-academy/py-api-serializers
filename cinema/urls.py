from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MoviesViewSet,
    MovieSessionViewSet
)


app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MoviesViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls
