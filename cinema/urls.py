from django.urls import path, include
from rest_framework import routers

from cinema import views
app_name = "cinema"

router = routers.DefaultRouter()
router.register("actors", views.ActorViewSet, basename="actors")
router.register("genres", views.GenreViewSet, basename="genres")
router.register("cinema_halls", views.CinemaHallViewSet, basename="cinema_halls")
router.register("movies", views.MovieViewSet, basename="movies")
router.register("movies_sessions", views.MovieSessionViewSet, basename="movies_sessions")
urlpatterns = [
    path("", include(router.urls))
]
