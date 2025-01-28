from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related("actors", "genres")
        if self.action == "retrieve":
            queryset = queryset.prefetch_related("actors", "genres")

        return queryset

    def get_serializer_class(self) -> [
        MovieSerializer,
        MovieListSerializer,
        MovieRetrieveSerializer
    ]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("movie", "cinema_hall")
        if self.action == "retrieve":
            return queryset.select_related("movie", "cinema_hall")

        return queryset

    def get_serializer_class(self) -> [
        MovieSessionSerializer,
        MovieSessionListSerializer,
        MovieSessionRetrieveSerializer
    ]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
