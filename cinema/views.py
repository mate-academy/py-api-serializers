from rest_framework import viewsets

from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSessionSerrializer,
    MovieSessionListSerrializeer,
    MovieSessionDetailSerializer,
    CinemaHallSerializer
)
from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return self.serializer_class


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerrializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerrializeer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return self.serializer_class


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
