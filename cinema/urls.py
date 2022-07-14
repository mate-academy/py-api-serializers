from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallView,
    GenreView,
    ActorView,
    MovieView,
    MovieSessionView
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallView)
router.register("genres", GenreView)
router.register("actors", ActorView)
router.register("movies", MovieView)
router.register("movie_sessions", MovieSessionView)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
