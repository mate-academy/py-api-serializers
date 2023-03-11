from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework import serializers
from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    MovieSession, Movie
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSerializer,
    MovieSessionDetailSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors").prefetch_related("genres")
        return queryset

    def get_serializer_class(self) -> serializers:
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie").select_related("cinema_hall")
        return queryset

    def get_serializer_class(self) -> serializers:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer
