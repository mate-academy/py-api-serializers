from django.urls import path, include
from rest_framework import routers

from cinema import views

app_name = "cinema-api"

router = routers.DefaultRouter()

router.register(r"genres", views.GenreViewSet, basename="genres")
router.register(r"actors", views.ActorViewSet, basename="actors")
router.register(
    r"cinema_halls", views.CinemaHallViewSet, basename="cinema-halls"
)
router.register(r"movies", views.MovieViewSet, basename="movies")
router.register(
    r"movie_sessions", views.MovieSessionViewSet, basename="movie_sessions"
)


urlpatterns = [
    path("", include(router.urls)),
]
