from django.urls import path, include
from rest_framework import routers

from cinema.views import GenreViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")

urlpatterns = [
    path("", include(router.urls)),

]

app_name = "cinema"
