from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet,
    OrderViewSet,
    TicketViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

app_name = "cinema"

router = routers.SimpleRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
