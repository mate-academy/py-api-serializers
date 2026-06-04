# write urls here
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
    OrderViewSet,
    TicketViewSet, CinemaHallViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = router.urls

app_name = "cinema"
