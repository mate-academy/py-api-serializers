# write urls here
from rest_framework import routers

from cinema.views import (ActorViewSet,
                          MovieViewSet,
                          MovieSessionViewSet,
                          CinemaHallViewSet,
                          GenreViewSet)

router = routers.DefaultRouter()
router.register(
    r"actors", ActorViewSet, basename="actor"
)
router.register(
    r"genres", GenreViewSet, basename="genre"
)
router.register(
    r"cinema_halls", CinemaHallViewSet, basename="cinema_hall"
)
router.register(
    r"movies", MovieViewSet, basename="movie"
)
router.register(
    r"movie_sessions", MovieSessionViewSet, basename="movie_session")

urlpatterns = router.urls
