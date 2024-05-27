from django.urls import path

from cinema.views import (
    TicketViewSet,
    GenreViewSet,
    OrderViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet
)

app_name = "cinema"

urlpatterns = [
    path("tickets/", TicketViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="ticket-list"),
    path("tickets/<int:pk>/", TicketViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="ticket-detail"),
    path("actors/", ActorViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="actor-list"),
    path("actors/<int:pk>/", ActorViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="actor-detail"),
    path("genres/", GenreViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="genre-list"),
    path("genres/<int:pk>/", GenreViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="genre-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="cinema_halls-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="cinema_halls-detail"),
    path("orders/", OrderViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="order-list"),
    path("orders/<int:pk>/", OrderViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="order-detail"),
    path("movies/", MovieViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="movie-list"),
    path("movies/<int:pk>/", MovieViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="movie-detail"),
    path("movie_sessions/", MovieSessionViewSet.as_view(
        {
            "get": "list",
            "post": "create"
        }
    ), name="movie_session-list"),
    path("movie_sessions/<int:pk>/", MovieSessionViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="movie_session-detail"),
]
