from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema import views

app_name = "cinema"

router = DefaultRouter()
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("movies", views.MovieViewSet)
router.register("cinema_halls", views.CinemaHallViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
