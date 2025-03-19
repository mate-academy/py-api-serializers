from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (CinemaHallSerializer,
                                ActorSerializer,
                                GenreSerializer, MovieSerializer,
                                MovieSessionSerializer, MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionListSerializer,
                                MovieSessionsRetrieveSerializer)


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
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")

        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionsRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list",):
            queryset = queryset.prefetch_related("movie", "cinema_hall")

        return queryset
