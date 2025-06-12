from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet
)


router = DefaultRouter()
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "genres",
    GenreViewSet,
    basename="genres"
)
router.register(
    "actors",
    ActorViewSet,
    basename="actors"
)
router.register(
    "movies",
    MovieViewSet,
    basename="movies"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register(
    "orders",
    OrderViewSet,
    basename="orders"
)
router.register(
    "tickets",
    TicketViewSet,
    basename="tickets"
)


urlpatterns = [
    path("", include(router.urls))
]


app_name = "cinema"
