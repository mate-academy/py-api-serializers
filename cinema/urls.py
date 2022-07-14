from django.urls import path, include
from rest_framework import routers

from cinema.views import MoviesViewSet, ActorsViewSet, GenresViewSet, \
    CinemaHallsViewSet, MovieSessionsViewSet

router = routers.DefaultRouter()
router.register("movies", MoviesViewSet)
router.register("actors", ActorsViewSet)
router.register("genres", GenresViewSet)
router.register("cinema_halls", CinemaHallsViewSet)
router.register("movie_sessions", MovieSessionsViewSet)

urlpatterns = [
    path("", include(router.urls))

]

app_name = "cinema"
