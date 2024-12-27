from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("genres", viewset=GenreViewSet, basename="genres")
router.register("movies", viewset=MovieViewSet, basename="movies")
router.register("actors", viewset=ActorViewSet, basename="actors")
router.register(
    "cinema_halls",
    viewset=CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movie_sessions",
    viewset=MovieSessionViewSet,
    basename="movie_sessions"
)
urlpatterns = [
    path("", include(router.urls)),
    path("app/cinema/", include(router.urls)),
]
