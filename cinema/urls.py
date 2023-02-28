from django.urls import path, include
from rest_framework import routers

from cinema.views import CinemaHallViewSet, GenreViewSet, ActorViewSet, \
    MovieViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]
