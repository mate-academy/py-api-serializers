from django.urls import include, path
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          MovieSessionViewSet,
                          ActorViewSet,
                          GenreViewSet,
                          CinemaHallViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
