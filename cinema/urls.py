from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

routers = routers.DefaultRouter()
routers.register("genres", GenreViewSet)
routers.register("movies", MovieViewSet)
routers.register("movie_sessions", MovieSessionViewSet)
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(routers.urls)),
]

app_name = "cinema"
