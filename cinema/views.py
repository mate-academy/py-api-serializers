from django.db.models import QuerySet
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
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
    serializer_class = MovieListSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> Serializer:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> Serializer:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action == "list":
            return queryset.select_related("movie", "cinema_hall")
        elif self.action == "retrieve":
            return queryset.select_related("cinema_hall").prefetch_related(
                "movie__genres", "movie__actors"
            )
        return queryset
