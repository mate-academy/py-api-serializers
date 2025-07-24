from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import GenreViewSet, MovieViewSet, MovieSessionViewSet, CinemaHallViewSet, ActorViewSet

app_name = "cinema"

router = DefaultRouter()

router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("",include(router.urls)),
]
