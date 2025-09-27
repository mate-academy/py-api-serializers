from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, CinemaHallViewSet, MovieSessionViewSet, GenreViewSet, ActorViewSet

app_name = "cinema"

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_session")

urlpatterns = [
    path("", include(router.urls)),
]