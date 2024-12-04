from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [path("", include(router.urls))]
