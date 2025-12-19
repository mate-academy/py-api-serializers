from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (GenreViewSet,
                          ActorViewSet,
                          MovieViewSet,
                          MovieSessionViewSet,
                          CinemaHallsViewSet)

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallsViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
