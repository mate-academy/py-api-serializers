from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
)


router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls
