from rest_framework import routers

from cinema.views import CinemaHallViewSet

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
