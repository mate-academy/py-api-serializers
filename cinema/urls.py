from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (ActorsViewSet,
                          MovieSessionsViewSet,
                          GenresViewSet,
                          CinemaHallsViewSet,
                          MoviesViewSet)

router = DefaultRouter()
router.register("actors", ActorsViewSet)
router.register("genres", GenresViewSet)
router.register("cinema_halls", CinemaHallsViewSet)
router.register("movies", MoviesViewSet)
router.register("movie_sessions", MovieSessionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
