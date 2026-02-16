from django.urls import path, include

from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)
from rest_framework import routers

app_name = "station"

router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
