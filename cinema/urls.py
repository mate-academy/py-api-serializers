
from rest_framework import routers
from django.urls import path, include

from cinema.views import GenreViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
