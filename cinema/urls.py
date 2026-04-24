from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieSessionViewSet,
                          TicketViewSet)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
