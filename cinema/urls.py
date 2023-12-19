from django.urls import path, include
from rest_framework import routers

from cinema.views import (ActorViewSet,
                          GenreViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"

