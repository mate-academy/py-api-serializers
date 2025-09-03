from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema import views  # твій додаток з views.py

router = DefaultRouter()
router.register(r"movies", views.MovieViewSet, basename="movie")
router.register(r"actors", views.ActorViewSet, basename="actor")
router.register(r"genres", views.GenreViewSet, basename="genre")
router.register(r"moviesessions", views.MovieSessionViewSet, basename="moviesession")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
