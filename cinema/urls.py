from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-hall"
)
router.register(
    "genres",
    GenreViewSet,
    basename="genre"
)
router.register(
    "actors",
    ActorViewSet,
    basename="actor"
)
router.register(
    "movies",
    MovieViewSet,
    basename="movie"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)


urlpatterns = router.urls
