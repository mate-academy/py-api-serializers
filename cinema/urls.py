from django.urls import path, include
from rest_framework import routers

from cinema import views
app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")
urlpatterns = [
    path("", include(router.urls))
]
