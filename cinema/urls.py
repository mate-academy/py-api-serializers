from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreViewSet, ActorViewSet, MovieSessionViewSet, MovieViewSet, CinemaHallViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
