from django.db.models import QuerySet
from rest_framework import (
    viewsets,
)

from rest_framework.serializers import Serializer

from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieRetrieveSerializer,
    MovieCreateUpdateSerializer,
)

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)


class GenreViewSet(
    viewsets.ModelViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(
    viewsets.ModelViewSet
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    viewsets.ModelViewSet
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(
    viewsets.ModelViewSet
):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related(
                "genres",
                "actors",
            )
        return queryset

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieRetrieveSerializer
        if (
            self.action == "create"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            return MovieCreateUpdateSerializer

        return MovieSerializer


class MovieSessionViewSet(
    viewsets.ModelViewSet
):
    queryset = MovieSession.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.select_related(
                "movie",
                "cinema_hall",
            )

        return queryset

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
