from rest_framework.routers import DefaultRouter

from .views import (
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
