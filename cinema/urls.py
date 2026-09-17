from django.urls import include, path
from rest_framework import routers

from .views import (MovieViewSet,
                    GenreViewSet,
                    ActorViewSet,
                    CinemaHallViewSet,
                    MovieSessionViewSet)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
