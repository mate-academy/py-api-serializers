from rest_framework import routers

from cinema import views

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")
router.register("actors", views.ActorViewSet, basename="actors")
router.register("genres", views.GenreViewSet, basename="genres")
router.register(
    "movie_sessions",
    views.MovieSessionViewSet,
    basename="movie-sessions"
)
router.register(
    "cinema_halls",
    views.CinemaHallViewSet,
    basename="cinema-halls"
)

urlpatterns = router.urls
