from django.urls import path, include
from rest_framework import routers


from cinema.views import ActorViewSet, GenreViewSet


router = routers.DefaultRouter()
router.register("actor", ActorViewSet)
router.register("genre", GenreViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
