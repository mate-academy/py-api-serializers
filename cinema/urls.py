from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls)),
]
