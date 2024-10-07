from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)


urlpatterns = [
    path("cinema/", include(router.urls)),

]

app_name = "cinema"
