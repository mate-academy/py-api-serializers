from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router_genres = routers.DefaultRouter()
router_genres.register("genres", GenreViewSet)

router_actors = routers.DefaultRouter()
router_actors.register("actors", ActorViewSet)

router_cinema_halls = routers.DefaultRouter()
router_cinema_halls.register("cinema_halls", CinemaHallViewSet)

router_movies = routers.DefaultRouter()
router_movies.register("movies", MovieViewSet)

router_movie_sessions = routers.DefaultRouter()
router_movie_sessions.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router_genres.urls)),
    path("", include(router_actors.urls)),
    path("", include(router_cinema_halls.urls)),
    path("", include(router_movies.urls)),
    path("", include(router_movie_sessions.urls)),
]

app_name = "cinema"
