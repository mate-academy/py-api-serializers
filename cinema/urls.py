from rest_framework import routers

from cinema.views import (
    AuthorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("actors", AuthorViewSet)
router.register("genres", GenreViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
