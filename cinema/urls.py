from rest_framework.routers import DefaultRouter

from cinema.views import (MovieSessionViewSet, CinemaHallViewSet,
                          GenreViewSet, ActorViewSet, MovieViewSet)

app_name = "cinema"

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)
urlpatterns = [] + router.urls
