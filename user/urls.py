from django.urls import include, path
from rest_framework import routers

from user.views import (
    MovieSessionViewSet,
    ActorViewSet,
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "user"
