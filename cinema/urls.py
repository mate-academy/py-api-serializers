from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (MovieViewSet,
                          CinemaHallViewSet,
                          ActorViewSet,
                          GenreViewSet,
                          MovieSessionViewSet)

router = DefaultRouter()
router.register("movies", viewset=MovieViewSet)
router.register("cinema_halls", viewset=CinemaHallViewSet)
router.register("actors", viewset=ActorViewSet)
router.register("genres", viewset=GenreViewSet)
router.register("movie_sessions", viewset=MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
