from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreViewSet

router = DefaultRouter()


router.register("genre", GenreViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
