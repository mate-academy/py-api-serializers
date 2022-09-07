from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cinema.views import ActorViewSet, CinemaHallViewSet, GenreViewSet, MovieSessionViewSet, MovieViewSet

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movies")
router.register("movie_sessions", MovieSessionViewSet, basename="movie-sessions")


urlpatterns = [
    path("", include(router.urls))
]
