from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)


urlpatterns = router.urls

app_name = "cinema"
