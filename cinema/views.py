from django.db.models import QuerySet, Manager
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, Actor, CinemaHall, Genre, MovieSession
from cinema.serializers import (CinemaHallSerializer,
                                MovieListSerializer,
                                MovieSessionListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionRetrieveSerializer,
                                ActorSerializer,
                                GenreSerializer,
                                MovieSessionSerializer,
                                MovieSerializer)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer
