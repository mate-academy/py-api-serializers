from rest_framework import routers
from django.urls import path, include
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)


router = routers.DefaultRouter()
router.register(prefix="genres", viewset=GenreViewSet)
router.register(prefix="actors", viewset=ActorViewSet)
router.register(prefix="cinema_halls", viewset=CinemaHallViewSet)
router.register(prefix="movies", viewset=MovieViewSet)
router.register(prefix="movie_sessions", viewset=MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
