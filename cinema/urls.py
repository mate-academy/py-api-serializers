from rest_framework.routers import DefaultRouter

from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet,
    GenreViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie_session"
)
router.register("orders", OrderViewSet, basename="order")
router.register("tickets", TicketViewSet, basename="ticket")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = router.urls

app_name = "cinema"
