from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = SimpleRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls))
]
