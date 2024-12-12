from django.urls import path, include
from cinema import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    "cinema_halls", views.CinemaHallViewSet, basename="cinema_halls"
)
router.register("genres", views.GenreViewSet, basename="genres")
router.register("actors", views.ActorViewSet, basename="actors")
router.register("movies", views.MovieViewSet, basename="movies")
router.register(
    "movie_sessions", views.MovieSessionViewSet, basename="movie_sessions"
)
router.register("orders", views.OrderViewSet, basename="orders")
router.register("tickets", views.TicketViewSet, basename="tickets")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
