from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

routers = routers.DefaultRouter()
routers.register("actors", ActorViewSet)
routers.register("genres", GenreViewSet)
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("movies", MovieViewSet)
routers.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(routers.urls)),
]

app_name = "cinema"
