from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    GenreViewSet,
)


router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
