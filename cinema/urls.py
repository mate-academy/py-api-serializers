from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = router.urls

app_name = "cinema"
