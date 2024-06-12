from rest_framework.routers import DefaultRouter

from cinema.views import (
    CinemaHallView,
    GenreView,
    MovieView,
    MovieSessionView,
    ActorView,
)

router = DefaultRouter()

router.register("cinema_halls", CinemaHallView)
router.register("genres", GenreView)
router.register("movies", MovieView)
router.register("movie_sessions", MovieSessionView)
router.register("actors", ActorView)


urlpatterns = router.urls

app_name = "cinema"
