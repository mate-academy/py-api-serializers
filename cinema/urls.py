from rest_framework import routers

from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [] + router.urls

app_name = "cinema"
