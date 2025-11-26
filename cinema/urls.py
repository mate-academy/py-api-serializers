from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


app_name = "cinema"

router = DefaultRouter()
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
