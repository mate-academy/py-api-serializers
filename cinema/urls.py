from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet, MovieSessionViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'cinema_halls', CinemaHallViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'movie_sessions', MovieSessionViewSet)

urlpatterns = [
    path('api/cinema/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'cinema'
