from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cinema import views
from cinema.views import CinemaHallViewSet

app_name = 'cinema'
router = routers.DefaultRouter()
router.register('movie', views.MovieViewSet)
router.register('actors', views.ActorViewSet)
router.register('genres', views.GenreViewSet)
router.register('halls', views.CinemaHallViewSet)
router.register('movie_session', views.MovieSessionViewSet)
urlpatterns = [path("", include(router.urls)),]
