from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          CinemaHallViewSet,
                          MovieViewSet,
                          MovieSessionViewSet)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="manage")
router.register("actors", ActorViewSet, basename="manage")
router.register("cinema_halls", CinemaHallViewSet, basename="manage")
router.register("movies", MovieViewSet, basename="manage")
router.register("movie_sessions", MovieSessionViewSet, basename="manage")
urlpatterns = router.urls
path("",
     include(router.urls)),

app_name = "cinema"
