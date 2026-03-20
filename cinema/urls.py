from rest_framework.routers import DefaultRouter

from cinema.views import CinemaHallViewSet, ActorsViewSet, GenreViewSet, MovieViewSet, MovieSessionViewSet

router = DefaultRouter()
router.register('cinema_halls', CinemaHallViewSet)
router.register('actors', ActorsViewSet)
router.register('genres', GenreViewSet)
router.register('movies', MovieViewSet)
router.register('movie_sessions', MovieSessionViewSet)
urlpatterns = router.urls
