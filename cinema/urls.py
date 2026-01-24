from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet
)

router = DefaultRouter()
router.register(r'cinema/cinema_halls', CinemaHallViewSet)
router.register(r'cinema/genres', GenreViewSet)
router.register(r'cinema/actors', ActorViewSet)
router.register(r'cinema/movies', MovieViewSet)
router.register(r'cinema/movie_sessions', MovieSessionViewSet)
router.register(r'cinema/orders', OrderViewSet)
router.register(r'cinema/tickets', TicketViewSet)

urlpatterns = [
    path('cinema/', include(router.urls)),
]
