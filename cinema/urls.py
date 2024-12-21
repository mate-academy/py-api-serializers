from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    TicketViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = []

urlpatterns += router.urls
