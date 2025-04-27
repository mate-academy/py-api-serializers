from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)

from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
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

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Movie.objects.all()
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("genres", "actors")

        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = MovieSession.objects.all()
        if self.action in ["list", "retrieve"]:
            return queryset.select_related("movie", "cinema_hall")

        return queryset
