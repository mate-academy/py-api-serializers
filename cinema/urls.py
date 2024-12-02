from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
app_name = "cinema"
