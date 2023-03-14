from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),

]

app_name = "cinema"
