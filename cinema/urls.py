from rest_framework import routers

from .views import (CinemaHallViewSet,
                    GenreViewSet,
                    ActorViewSet,
                    MovieViewSet,
                    MovieSessionViewSet
                    )


router = routers.SimpleRouter()
router.register(
    r"cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(r"genres", GenreViewSet, basename="genres")
router.register(r"actors", ActorViewSet, basename="actors")
router.register(r"movies", MovieViewSet, basename="movies")
router.register(
    r"movie_sessions",
    MovieSessionViewSet,
    basename="movie_sessions"
)

urlpatterns = router.urls
