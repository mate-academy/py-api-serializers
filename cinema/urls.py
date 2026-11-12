from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet, CinemaHallViewSet, MovieViewSet
)


router = DefaultRouter()


router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
