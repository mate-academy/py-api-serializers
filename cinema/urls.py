# write urls here
from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    TicketViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
