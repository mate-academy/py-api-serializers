from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreViewSet

genre_router = routers.DefaultRouter()
genre_router.register("genres", GenreViewSet, basename="genres")


urlpatterns = [
    path("", include(genre_router.urls))
]

app_name = "cinema"
