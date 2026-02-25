from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet

app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("", include(router.urls))

]