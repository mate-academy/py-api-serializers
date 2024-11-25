from django.urls import include, path
from rest_framework import routers

from cinema import views

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("cinema_halls", views.CinemaHallViewSet)
router.register("movies", views.MovieViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)

urlpatterns = [path("", include(router.urls))]
