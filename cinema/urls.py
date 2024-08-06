from django.urls import path, include
from rest_framework import routers

from cinema import views


router = routers.DefaultRouter()

router.register("cinema_halls", views.CinemaHallViewSet)
router.register("genres", views.GenreViewSet)
router.register("actors", views.ActorViewSet)
router.register("movies", views.MovieViewSet)
router.register("movie_sessions", views.MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
