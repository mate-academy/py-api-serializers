from django.urls import path, include
from rest_framework import routers
from cinema.views import (MovieSet,
                          ActorSet,
                          GenreSet,
                          CinemaHallSet,
                          MovieSessionSet)

router = routers.DefaultRouter()
router.register("movies", MovieSet)
router.register("actors", ActorSet)
router.register("genres", GenreSet)
router.register("cinema_halls", CinemaHallSet)
router.register("movie_sessions", MovieSessionSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
