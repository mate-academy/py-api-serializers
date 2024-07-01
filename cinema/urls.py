from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions",
                MovieSessionViewSet,
                basename="movie-session")
router.register("orders", OrderViewSet, basename="order")
router.register("tickets", TicketViewSet, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
]
