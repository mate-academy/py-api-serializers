from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls))
]
app_name = "cinema"
