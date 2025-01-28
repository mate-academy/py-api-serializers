from django.contrib.admin.widgets import url_params_from_lookup_dict
from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
