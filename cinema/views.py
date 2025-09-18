from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (CinemaHallSerializer, GenreSerializer,
                                ActorSerializer, MovieSessionSerializer,
                                MovieSerializer, MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = Movie.objects.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = MovieSession.objects.select_related(
                "movie", "cinema_hall")
        return queryset
