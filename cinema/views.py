from django.db.models.query import QuerySet
from rest_framework import viewsets

from cinema.models import Actor, CinemaHall, Movie, MovieSession, Genre
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    GenreSerializer,
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
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> MovieSerializer:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self) -> MovieSessionSerializer:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
