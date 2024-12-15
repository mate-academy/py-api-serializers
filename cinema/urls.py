from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
