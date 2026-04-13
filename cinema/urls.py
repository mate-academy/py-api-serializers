from rest_framework.routers import DefaultRouter
from .views import (GenreViewSet,
                    ActorViewSet,
                    MovieViewSet,
                    CinemaHallViewSet,
                    MovieSessionViewSet)

router = DefaultRouter()
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"actors", ActorViewSet, basename="actor")
router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"movie_sessions",
                MovieSessionViewSet,
                basename="movie_sessions")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")

urlpatterns = router.urls
