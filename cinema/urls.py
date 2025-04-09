from rest_framework import routers
from django.urls import include, path
from .views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
