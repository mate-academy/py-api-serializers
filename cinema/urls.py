from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
