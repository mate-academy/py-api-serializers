from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("cinema_halls", views.CinemaHallViewSet)
router.register("movies", views.MovieViewSet, basename="movie")
router.register(
    "movie_sessions",
    views.MovieSessionViewSet,
    basename="movie_session"
)

urlpatterns = router.urls


app_name = "cinema"
