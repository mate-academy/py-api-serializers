import debug_toolbar
from django.urls import include, path
from rest_framework import routers


from cinema.views import (
    MovieViewSet,
    ActorViewSet,
    GenreViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("Genres", GenreViewSet)
router.register("Movie", MovieViewSet)
router.register("CinemaHall", CinemaHallViewSet)


movie_session_list = MovieSessionViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
movie_session_detail = MovieSessionViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

movie_list = MovieViewSet.as_view(actions={"get": "list", "post": "create"})
movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

genre_list = GenreViewSet.as_view(actions={"get": "list", "post": "create"})
genre_hall_detail = GenreViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

actor_list = ActorViewSet.as_view(actions={"get": "list", "post": "create"})
actor_detail = ActorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    # path("", include(router.urls)),
    path(
        "api/cinema/genres/",
        genre_list,
        name="genre_list"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        genre_hall_detail,
        name="genre_detail"
    ),
    path(
        "api/cinema/movies/",
        movie_list,
        name="movie_list"
    ),
    path(
        "api/cinema/movies/<int:pk>/",
        movie_detail,
        name="movie_detail"
    ),
    path(
        "api/cinema/cinema_halls/",
        cinema_hall_list,
        name="cinema_hall_list"
    ),
    path(
        "api/cinema/cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_detail"
    ),
    path(
        "api/cinema/actors/",
        actor_list,
        name="actor_list"
    ),
    path(
        "api/cinema/actors/<int:pk>/",
        actor_detail,
        name="actor_detail"
    ),
    path(
        "api/cinema/movie_sessions/",
        movie_session_list,
        name="movie_session_list"
    ),
    path(
        "api/cinema/movie_sessions/<int:pk>/",
        movie_session_detail,
        name="movie_session_detail"
    ),
]

app_name = "cinema"
