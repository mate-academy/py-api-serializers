from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)

urlpatterns = router.urls

app_name = "cinema"
