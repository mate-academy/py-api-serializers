from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register("cinema/actors", ActorViewSet)
router.register("cinema/genres", GenreViewSet)
router.register("cinema/cinema_halls", CinemaHallViewSet)
router.register("cinema/movies", MovieViewSet)
router.register("cinema/movie_sessions", MovieSessionViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls)),
]
