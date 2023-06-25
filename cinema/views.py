from rest_framework import viewsets

from cinema.models import CinemaHall, MovieSession, Movie, Genre, Actor
from cinema.serializers import (
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieListSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieDetailSerializer,
    MovieSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action in "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("cinema_hall", "movie").all()

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action in "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer
