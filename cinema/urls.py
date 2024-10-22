from django.urls import path, include

from rest_framework import routers


from cinema.views import (
    CinemaHallViewSet,
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    TicketViewSet,
    OrderViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
