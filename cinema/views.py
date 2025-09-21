from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from .models import Movie, MovieSession, Genre, Actor, CinemaHall
from .serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    ActorSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    _prefetch_fields_actions = ["list", "retrieve"]

    def get_serializer_class(self) -> type(Serializer):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    _prefetch_fields_actions = ["list", "retrieve"]

    def get_serializer_class(self) -> type(Serializer):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset

        if self.action in self._prefetch_fields_actions:
            return queryset.select_related("movie", "cinema_hall")

        return queryset.all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
