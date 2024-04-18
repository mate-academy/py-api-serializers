from rest_framework import viewsets

from cinema.models import Movie, Actor, CinemaHall, Genre, MovieSession
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.select_related()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.select_related()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.prefetch_related("genres")

        return queryset


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.select_related()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related()
    serializer_class = MovieSessionListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related()

        return queryset
