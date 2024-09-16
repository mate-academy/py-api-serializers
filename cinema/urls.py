from rest_framework import routers

from django.urls import path, include

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

routers = routers.DefaultRouter()
routers.register("genres", GenreViewSet)
routers.register("actors", ActorViewSet)
routers.register("movies", MovieViewSet)
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(routers.urls))
]

app_name = "cinema"
