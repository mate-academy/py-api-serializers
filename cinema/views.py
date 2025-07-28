from rest_framework import viewsets

from cinema.models import Genre, CinemaHall, Movie, MovieSession, Actor
from cinema.serializers import (
    GenreSerializer, ActorSerializer,
    CinemaHallSerializer, MovieListSerializer,
    MovieDetailSerializer, MovieCreateUpdateSerializer,
    MovieSessionDetailSerializer, MovieSessionListSerializer,
    MovieSessionCreateSerializer, ActorCreateUpdateSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ActorCreateUpdateSerializer
        return ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer

        return MovieCreateUpdateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        elif self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionDetailSerializer
