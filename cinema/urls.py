from django.urls import path, include
from rest_framework import routers
from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          MovieViewSet,
                          CinemaHallViewSet,
                          MovieSessionViewSet,
                          OrderViewSet,
                          TicketViewSet)


app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
]