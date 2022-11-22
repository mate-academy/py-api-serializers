from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"genres",
    GenreViewSet,
    basename="genre"
)
router.register(
    r"movies",
    MovieViewSet,
    basename="movie"
)
router.register(
    r"actors",
    ActorViewSet,
    basename="actor"
)
router.register(
    r"cinema_halls",
    CinemaHallViewSet,
    basename="cinema_hall"
)
router.register(
    r"movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)


urlpatterns = router.urls


app_name = "cinema"
