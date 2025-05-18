from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    GenreViewSet, ActorViewSet, CinemaHallViewSet,
    MovieViewSet, MovieSessionViewSet
)

router = DefaultRouter()
router.register(r"cinema/genres", GenreViewSet)
router.register(r"cinema/actors", ActorViewSet)
router.register(r"cinema/cinema_halls", CinemaHallViewSet)
router.register(r"cinema/movies", MovieViewSet)
router.register(r"cinema/movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
