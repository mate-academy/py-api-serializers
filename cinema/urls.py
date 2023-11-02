from rest_framework import routers

from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet, \
    MovieViewSet, MovieSessionViewSet

router = routers.DefaultRouter()
router.register("genre", GenreViewSet)
router.register("actor", ActorViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("movie", MovieViewSet)
router.register("movie_session", MovieSessionViewSet)

urlpatterns = [] + router.urls

app_name = "cinema"
