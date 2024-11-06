from django.urls import path, include
from rest_framework import routers


from cinema.views import (
    CinemaHallViewSet,
    MovieSessionViewSet, MovieViewSet, ActorViewSet, GenreViewSet,
)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)

urlpatterns = [
    path("cinema/", include(router.urls)),
]
