from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)

list_actions = {"get": "list", "post": "create"}
retrieve_actions = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
}
actor_list = ActorViewSet.as_view(actions=list_actions)
actor_detail = ActorViewSet.as_view(
    actions=retrieve_actions
)

genre_list = GenreViewSet.as_view(actions=list_actions)
genre_detail = GenreViewSet.as_view(
    actions=retrieve_actions
)
cinema_hall_list = CinemaHallViewSet.as_view(actions=list_actions)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions=retrieve_actions
)
movie_list = MovieViewSet.as_view(actions=list_actions)
movie_detail = MovieViewSet.as_view(
    actions=retrieve_actions
)
movie_session_list = MovieSessionViewSet.as_view(
    actions=list_actions
)
movie_session_detail = MovieSessionViewSet.as_view(
    actions=retrieve_actions
)
router = routers.DefaultRouter()
router.register(prefix="actors", viewset=ActorViewSet)
router.register(prefix="genres", viewset=GenreViewSet)
router.register(prefix="movies", viewset=MovieViewSet)
router.register(prefix="movie_sessions", viewset=MovieSessionViewSet)

urlpatterns = [
    path("actors/", actor_list, name="actor-list"),
    path("actors/<int:pk>/", actor_detail, name="actor-detail"),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall-detail"
    ),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("movie_sessions/", movie_session_list, name="movie_session-list"),
    path(
        "movie_sessions/<int:pk>/",
        movie_session_detail,
        name="movie_session-detail"
    ),
]

app_name = "cinema"
