from django.urls import path, include
from rest_framework import routers

from cinema import views


router = routers.DefaultRouter()

router.register(prefix="movies", viewset=views.MovieViewSet)
router.register(prefix="movie_sessions", viewset=views.MovieSessionViewSet)
router.register(prefix="cinema_halls", viewset=views.CinemaHallViewSet)
router.register(prefix="actors", viewset=views.ActorViewSet)
router.register(prefix="genres", viewset=views.GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
