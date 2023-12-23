from django.urls import path, include

from rest_framework import routers
from .views import (
    GenreViewsSet,
    ActorViewsSet,
    CinemaHallViewsSet,
    MovieViewsSet,
    MovieSessionViewsSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewsSet)
router.register("movies", MovieViewsSet)
router.register("actors", ActorViewsSet)
router.register("cinema_halls", CinemaHallViewsSet)
router.register("movie_sessions", MovieSessionViewsSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
