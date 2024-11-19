from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

cinema_hall_router = routers.DefaultRouter()
genre_router = routers.DefaultRouter()
actor_router = routers.DefaultRouter()
movie_router = routers.DefaultRouter()
movie_session_router = routers.DefaultRouter()

cinema_hall_router.register("", CinemaHallViewSet)
genre_router.register("", GenreViewSet)
actor_router.register("", ActorViewSet)
movie_router.register("", MovieViewSet)
movie_session_router.register("", MovieSessionViewSet)

urlpatterns = [
    path("cinema_halls/", include(cinema_hall_router.urls)),
    path("genres/", include(genre_router.urls)),
    path("actors/", include(actor_router.urls)),
    path("movies/", include(movie_router.urls)),
    path("movie_sessions/", include(movie_session_router.urls)),
]

app_name = "cinema"
