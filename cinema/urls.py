from rest_framework import routers

from cinema.views import (
    CinemaHallSet,
    GenreSet,
    ActorSet,
    MovieSet,
    MovieSessionSet,
    OrderSet,
    TicketSet,
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallSet)
router.register("genres", GenreSet)
router.register("actors", ActorSet)
router.register("movies", MovieSet)
router.register("movie_sessions", MovieSessionSet)
router.register("orders", OrderSet)
router.register("tickets", TicketSet)
