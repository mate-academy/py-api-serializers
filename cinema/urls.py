from rest_framework.routers import DefaultRouter

from cinema.views import (MovieSessionViewSet, CinemaHallViewSet,
                          GenreViewSet, ActorViewSet, MovieViewSet)

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
urlpatterns = [] + router.urls
