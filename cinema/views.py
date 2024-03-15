from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        elif self.action == "create":
            return MovieCreateSerializer

        return MovieListSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        elif self.action == "create":
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
