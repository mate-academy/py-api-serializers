from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

routers = routers.DefaultRouter()
routers.register("genres", GenreViewSet, basename="genres")
routers.register("actors", ActorViewSet, basename="actors")
routers.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
routers.register("movies", MovieViewSet, basename="movies")
routers.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions"
)

urlpatterns = [
    path("", include(routers.urls))
]

app_name = "cinema"
