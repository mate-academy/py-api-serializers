from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer, MovieListSerializer, MovieDetailSerializer,
    MovieSessionListSerializer, MovieSessionDetailSerializer,
    GenreSerializer, ActorSerializer, CinemaHallSerializer,
    MovieSessionSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action == "create":
            return MovieSessionSerializer
        return MovieSessionListSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
