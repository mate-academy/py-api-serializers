from django.urls import path, include
from rest_framework import routers


from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionView,
)

router = routers.DefaultRouter()

router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions", MovieSessionView, basename="movie-session")


urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
