from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSets,
    GenreViewSets,
    CinemaHallViewSets,
    MovieViewSets,
    MovieSessionViewSets
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSets)
router.register("actors", ActorViewSets)
router.register("cinema_halls", CinemaHallViewSets)
router.register("movies", MovieViewSets)
router.register("movie_sessions", MovieSessionViewSets)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
