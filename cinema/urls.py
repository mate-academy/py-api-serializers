from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
genre = router.register("genres", GenreViewSet)
actor = router.register("actors", ActorViewSet)
cinema_hall = router.register("cinema_halls", CinemaHallViewSet)
movie = router.register("movies", MovieViewSet)
movie_session = router.register("movie_sessions", MovieSessionViewSet)


urlpatterns = [] + router.urls

app_name = "cinema"
