from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet,)

app_name = "cinema"

routers = DefaultRouter()
routers.register("genres", GenreViewSet)
routers.register("actors", ActorViewSet)
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("movies", MovieViewSet)
routers.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(routers.urls)),
    path("api/cinema/", include(routers.urls)),
]
