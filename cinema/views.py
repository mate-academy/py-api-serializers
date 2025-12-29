from typing import Type

from rest_framework import (
    serializers,
    viewsets
)

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionWriteSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieWriteSerializer
        return MovieListSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionListSerializer

    def get_serializer_class(self) -> Type[serializers.Serializer]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionWriteSerializer
        return MovieSessionListSerializer
