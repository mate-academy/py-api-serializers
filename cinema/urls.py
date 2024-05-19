from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

routers = routers.DefaultRouter()

routers.register("cinema_halls", CinemaHallViewSet)
routers.register("genres", GenreViewSet)
routers.register("actors", ActorViewSet),
routers.register("movies", MovieViewSet),
routers.register("movie_sessions", MovieSessionViewSet)

urlpatterns = routers.urls

app_name = "cinema"
