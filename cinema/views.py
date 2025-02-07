from rest_framework import viewsets
from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession
from cinema.serializers import (
    MovieListSerializer, MovieDetailSerializer, GenreSerializer,
    ActorSerializer, CinemaHallListSerializer, CinemaHallDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionSerializer,
    MovieCreateSerializer, MovieSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieCreateSerializer
        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CinemaHallListSerializer
        return CinemaHallDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
