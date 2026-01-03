from django.urls import path, include
from rest_framework import routers

from cinema import views

router = routers.DefaultRouter()
router.register(r"genres", views.GenreViewSet, basename="genre")
router.register(r"actors", views.ActorViewSet, basename="actor")
router.register(r"movies", views.MovieViewSet, basename="movie")
router.register(r"cinema_halls",
                views.CinemaHallViewSet, basename="cinema_hall")
router.register(r"movie_sessions",
                views.MovieSessionViewSet, basename="movie_session")

urlpatterns = [
    path("api/cinema/", include(router.urls)),
]
