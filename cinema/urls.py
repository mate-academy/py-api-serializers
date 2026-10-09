from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    MovieViewSet,

)
app_name = "cinema"
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
