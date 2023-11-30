from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieSessionViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorViewSet)
router.register("movie_sessions", MovieSessionViewSet)


urlpatterns = [

]
urlpatterns += router.urls
app_name = "cinema"
