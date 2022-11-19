from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genre", GenreViewSet)
