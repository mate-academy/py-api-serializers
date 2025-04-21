from django.urls import include, path
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          MovieSessionViewSet,
                          GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
