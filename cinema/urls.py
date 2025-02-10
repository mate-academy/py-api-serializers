from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)

app_name = "cinema"
urlpatterns = [
    path("", include(router.urls)),
]
