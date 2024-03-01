from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, CinemaHallViewSet, GenreViewSet, ActorViewSet, MovieSessionViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movies_session", MovieSessionViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)


urlpatterns = [
    # path("genres/", GenreList.as_view(), name="genre_list"),
    # path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    # path("actors/", ActorList.as_view(), name="actor_list"),
    # path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    # path("cinema_halls/", cinema_hall_list,
    #      name="cinema_halls_list"),
    # path("cinema_halls/<int:pk>/", cinema_hall_detail,
    #      name="cinema_halls_detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
