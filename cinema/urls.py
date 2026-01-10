from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    OrderViewSet,
    MovieViewSet,
    TicketViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet
)

router = routers.DefaultRouter()
router.register("orders", OrderViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("tickets", TicketViewSet)
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
