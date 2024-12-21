from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    CinemaHallsViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("genres", viewset=GenreViewSet, basename="genres")
router.register("actors", viewset=ActorViewSet, basename="actors")
router.register("movies", viewset=MovieViewSet, basename="movies")

router.register(
    "movie_sessions",
    viewset=MovieSessionViewSet,

)
router.register(
    "cinema_halls",
    viewset=CinemaHallsViewSet,
    basename="cinema-halls"
)
urlpatterns = [
    path("", include(router.urls)),
]
