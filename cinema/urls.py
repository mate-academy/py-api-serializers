from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
