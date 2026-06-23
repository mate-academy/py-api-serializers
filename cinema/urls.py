from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (GenreViewSet,
                          CinemaHallViewSet,
                          ActorViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
