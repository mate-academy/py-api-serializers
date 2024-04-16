from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="CinemaHall")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="MovieSession"
)

urlpatterns = router.urls

app_name = "cinema"
