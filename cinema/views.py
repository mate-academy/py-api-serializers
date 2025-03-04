from cinema.models import CinemaHall, Actor, Genre, Movie, MovieSession
from cinema.serializers import (
    CinemaHallSerializer,
    ActorSerializer,
    GenreSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)
from rest_framework import viewsets


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

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action in ["list", "retrieve"]:
            return self.queryset.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action in ["list", "retrieve"]:
            return self.queryset.prefetch_related("movie", "cinema_hall")
        return self.queryset
