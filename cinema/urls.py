from django.contrib import admin
from django.urls import path
from rest_framework import routers

from cinema.views import (ActorViewSet,
                          MovieViewSet,
                          GenreViewSet,
                          CinemaHallViewSet,
                          MovieSessionViewSet)

router = routers.DefaultRouter()

router.register("actors", ActorViewSet)

router.register("movies", MovieViewSet)

router.register("genres", GenreViewSet)

router.register("cinema_halls", CinemaHallViewSet)

router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
