from django.urls import path, include
from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    ActorViewSet,
    CinemaHallViewSet,

)
from rest_framework import routers


router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = router.urls

app_name = "cinema"
