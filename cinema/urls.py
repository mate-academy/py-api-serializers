from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (MovieViewSet,
                          GenreViewSet,
                          ActorViewSet,
                          MovieSessionViewSet,
                          CinemaHallViewSet
                          )

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"movie_sessions",
                MovieSessionViewSet,
                basename="movie_session"
                )
router.register(r"cinema_halls",
                CinemaHallViewSet,
                basename="cinema_hall"
                )
urlpatterns = [
    path("", include(router.urls)),
]


app_name = "cinema"
