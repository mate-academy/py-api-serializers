from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (MovieViewSet,
                          ActorViewSet,
                          GenreViewSet,
                          CinemaHallViewSet,
                          MovieSessionViewSet
                          )

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
