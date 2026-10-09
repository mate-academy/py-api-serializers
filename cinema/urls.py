from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)

urlpatterns = router.urls
