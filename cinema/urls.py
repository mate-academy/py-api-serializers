from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie_session"
)
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")

urlpatterns = router.urls

app_name = "cinema"
