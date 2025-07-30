from rest_framework import routers
from django.urls import path, include
from cinema.views import CinemaHallViewSet

from cinema.views import (
    CinemaHallViewSet, GenreViewSet, ActorViewSet,
    MovieViewSet, MovieSessionViewSet, OrderViewSet,
    TicketViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register(r'cinema/cinema_halls', CinemaHallViewSet, basename='cinema_halls')
router.register(r'cinema/genres', GenreViewSet, basename='genres')
router.register(r'cinema/actors', ActorViewSet, basename='actors')
router.register(r'cinema/movies', MovieViewSet, basename='movies')
router.register(r'cinema/movie_sessions', MovieSessionViewSet, basename='movie_sessions')
router.register(r'cinema/orders', OrderViewSet, basename='orders')
router.register(r'cinema/tickets', TicketViewSet, basename='tickets')

urlpatterns = [
    path('', include(router.urls)),
]
