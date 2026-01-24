from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

# OBSERVAÇÃO: Se você estiver usando este arquivo como cinema/urls.py e seu
# urls.py principal usa path("api/cinema/", include("cinema.urls")),
# as rotas ficarão no formato correto: api/cinema/movies/
