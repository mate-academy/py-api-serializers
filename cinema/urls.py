from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (CinemaHallViewSet,
                          MovieViewSet,
                          GenreViewSet,
                          ActorViewSet,
                          MovieSessionViewSet
                          )

router = DefaultRouter()
router.register(
    r"cinema/cinema_halls",
    CinemaHallViewSet,
    basename="cinemahall"
)
router.register(
    r"cinema/movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register(
    r"cinema/movies",
    MovieViewSet,
    basename="movie"
)
router.register(
    r"cinema/genres",
    GenreViewSet,
    basename="genre"
)
router.register(
    r"cinema/actors",
    ActorViewSet,
    basename="actor"
)

urlpatterns = [
    path("", include(router.urls)),
]
