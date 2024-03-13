from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)


default_router = routers.DefaultRouter()

default_router.register("movies", MovieViewSet)
default_router.register("genres", GenreViewSet)
default_router.register("actors", ActorViewSet)
default_router.register("cinema_halls", CinemaHallViewSet)
default_router.register("movies", MovieViewSet)
default_router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = default_router.urls

app_name = "cinema"
