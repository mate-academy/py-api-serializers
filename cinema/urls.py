from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet, CinemaHallViewSet
)


router = DefaultRouter()


router.register("genre", GenreViewSet)
router.register("actor", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
