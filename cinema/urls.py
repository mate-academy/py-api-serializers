from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet


app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls))
]
