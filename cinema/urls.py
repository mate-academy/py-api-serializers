from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet
)

router = routers.DefaultRouter()
routers.register("movies", MovieViewSet)
routers.register("genres", GenreViewSet)
routers.register("cinema_halls", CinemaHallViewSet)
routers.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"