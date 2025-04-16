from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    GenreModelViewSet,
    ActorModelViewSet,
    CinemaHallModelViewSet,
    MovieModelViewSet,
    MovieSessionModelViewSet
)

app_name = "cinema"
router = routers.DefaultRouter()
router.register("genres", GenreModelViewSet)
router.register("actors", ActorModelViewSet)
router.register("cinema_halls", CinemaHallModelViewSet)
router.register("movies", MovieModelViewSet, )
router.register("movie_sessions", MovieSessionModelViewSet)

urlpatterns = [
    path("cinema/", include(router.urls)),
]
