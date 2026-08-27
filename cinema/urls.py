from django.urls import path, include
from rest_framework import routers

from cinema.views import (ActorsViewSet, MovieViewSet, GenreViewSet,
                          MovieSessionViewSet, CinemaHallViewSet)

router = routers.DefaultRouter()

router.register(r"actors", ActorsViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls))
]
