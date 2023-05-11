from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenresView,
    ActorsView,
    CinemaHallsView,
    MovieView,
    MovieSessionView,
)

router = routers.DefaultRouter()

router.register("genres", GenresView)
router.register("actors", ActorsView)
router.register("cinema_halls", CinemaHallsView)
router.register("movies", MovieView)
router.register("movie_sessions", MovieSessionView)


urlpatterns = router.urls

app_name = "cinema"
