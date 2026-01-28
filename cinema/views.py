from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.db.models import QuerySet

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
    MovieRetrieveSerializer,
    MovieSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieSessionSerializer
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

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            self.serializer_class = MovieListSerializer
        elif self.action == "retrieve":
            self.serializer_class = MovieRetrieveSerializer
        elif self.action in ("create", "update", "partial_update"):
            self.serializer_class = MovieSerializer
        return self.serializer_class


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionListSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return self.queryset.select_related("movie", "cinema_hall")
        return self.queryset

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            self.serializer_class = MovieSessionListSerializer
        elif self.action == "retrieve":
            self.serializer_class = MovieSessionRetrieveSerializer
        elif self.action in ("create", "update", "partial_update"):
            self.serializer_class = MovieSessionSerializer
        return self.serializer_class
