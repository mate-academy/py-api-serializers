from django.urls import include, path
from rest_framework import routers

from cinema import views

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet)
router.register("cinema_halls", views.CinemaHallViewSet)
router.register("actors", views.ActorViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)
router.register("genres", views.GenreViewSet)

urlpatterns = [path("", include(router.urls))]
