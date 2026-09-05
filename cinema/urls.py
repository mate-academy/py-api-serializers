from rest_framework.routers import DefaultRouter
from cinema.views import (GenreViewSet, ActorViewSet, MovieViewSet,
                          CinemaHallViewSet, MovieSessionViewSet,
                          OrderViewSet, TicketViewSet)


router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = router.urls

app_name = "cinema"
