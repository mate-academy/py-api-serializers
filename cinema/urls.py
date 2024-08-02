from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieSessionViewSet
)


app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls
