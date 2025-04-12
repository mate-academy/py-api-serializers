from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
    # path("movies/", ..., name="movies_list"),
    # path("movies/<int:pk>/", ..., name="movies_detail"),
    # path("actors/", ..., name="actors_list"),
    # path("actors/<int:pk>/", ..., name="actors_detail"),
    # path("genres/", ..., name="genres_list"),
    # path("genres/<int:pk>/", ..., name="genres_detail"),
    # path("cinema_halls/", ..., name="cinema_halls_list"),
    # path("cinema_halls/<int:pk>/", ..., name="cinema_halls_detail"),
    # path("movie_sessions/", ..., name="movie_sessions_list"),
    # path("movie_sessions/<int:pk>/", ..., name="movie_sessions_detail"),
]

app_name = "cinema"
