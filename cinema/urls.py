# write urls here
from django.urls import include, path
from rest_framework import routers

from cinema.views import (CinemaHallViewSet, ActorViewSet,
                          GenreViewSet, MovieViewSet, MovieSessionViewSet)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
