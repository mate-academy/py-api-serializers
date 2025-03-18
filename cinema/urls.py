from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet

router = DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinemahalls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
