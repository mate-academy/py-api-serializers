from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet, MovieViewSet, OrderViewSet, ActorViewSet, MovieSessionViewSet, \
    TicketViewSet

app_name = "cinema"

router = routers.DefaultRouter()


router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [path("", include(router.urls))]
