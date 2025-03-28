from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
