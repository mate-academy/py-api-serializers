from django.urls import include, path
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          MovieSessionViewSet,
                          ActorSessionViewSet,
                          GenreSessionViewSet,
                          CinemaHallSessionViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorSessionViewSet)
router.register("genres", GenreSessionViewSet)
router.register("cinema_halls", CinemaHallSessionViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
