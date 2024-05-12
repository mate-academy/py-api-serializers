from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    GenreViewSet,
    CinemaHallsViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallsViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path('', include(router.urls))
]

app_name = "cinema"
