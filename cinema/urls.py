from rest_framework import routers


from cinema.views import (
    MovieViewSet,
    MovieSessionViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    ActorSeriaViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("actors", ActorSeriaViewSet)

urlpatterns = [] + router.urls

app_name = "cinema"
