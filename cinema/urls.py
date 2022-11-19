from django.urls import path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path(
        "genres/",
        GenreViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="actor-detail"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="cinema_hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="cinema_hall-detail"
    ),
    path(
        "movies/",
        MovieViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        MovieViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="movie-detail"
    ),
    path(
        "movie_sessions/",
        MovieSessionViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="movie_session-list"
    ),
    path(
        "movie_sessions/<int:pk>/",
        MovieSessionViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="movie_session-detail"
    ),
]

app_name = "cinema"
