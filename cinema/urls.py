from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
