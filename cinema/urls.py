from rest_framework import routers
from django.urls import path, include

from cinema import views

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet)
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)
router.register("cinema_halls", views.CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
