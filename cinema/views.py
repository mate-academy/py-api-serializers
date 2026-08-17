from django.db.models import QuerySet
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self) -> QuerySet[Movie]:
        return Movie.objects.prefetch_related(
            "genres",
            "actors",
        )

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer

        if self.action in (
            "create",
            "update",
            "partial_update",
        ):
            return MovieSerializer

        return MovieDetailSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self) -> QuerySet[MovieSession]:
        return (
            MovieSession.objects
            .select_related(
                "movie",
                "cinema_hall",
            )
            .prefetch_related(
                "movie__genres",
                "movie__actors",
            )
        )

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action in (
            "create",
            "update",
            "partial_update",
        ):
            return MovieSessionSerializer

        return MovieSessionDetailSerializer
