from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
