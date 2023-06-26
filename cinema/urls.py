from rest_framework import routers

from cinema.views import (
    CinemaHallViewSet,
    MovieSessionViewSet,
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

app_name = "cinema"

urlpatterns = router.urls
