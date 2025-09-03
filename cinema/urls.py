from django.urls import path, include
from rest_framework import routers
from cinema.views import (GenreViewSet,
                          ActorsViewSet,
                          MovieSessionViewSet,
                          MovieViewSet,
                          CinemaHallViewSet
                          )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorsViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
]


app_name = "cinema"
