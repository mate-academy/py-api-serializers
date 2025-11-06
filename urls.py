from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views.genre import GenreViewSet
from cinema.views.actor import ActorViewSet
from cinema.views.cinema_hall import CinemaHallViewSet
from cinema.views.movie import MovieViewSet
from cinema.views.movie_session import MovieSessionViewSet

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("api/cinema/", include(router.urls)),
]
