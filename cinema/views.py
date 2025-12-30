from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import Serializer

from .models import CinemaHall, Genre, Actor, Movie, MovieSession
from .serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieWriteSerializer,
    MovieDetailSerializer,
    MovieSessionWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action in ("create", "update"):
            return MovieWriteSerializer
        return MovieListSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionDetailSerializer

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionWriteSerializer
        return MovieSessionListSerializer
