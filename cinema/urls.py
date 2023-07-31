from django.urls import path, include
from rest_framework import routers


from cinema.views import ActorViewSet, GenreViewSet, CinemaHallViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register("actor", ActorViewSet, basename="actors")
router.register("genre", GenreViewSet, basename="genres")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
router.register("movies", MovieViewSet, basename="movies")


urlpatterns = [
    path("", include(router.urls))

]

app_name = "cinema"
