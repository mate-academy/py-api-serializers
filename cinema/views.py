from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Actor,
    Movie,
    MovieSession,
    Genre
)
from cinema.serializers import (
    CinemaHallSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


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
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("genres", "actors")

        return queryset


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
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return queryset.prefetch_related("cinema_hall", "movie")

        return queryset


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
