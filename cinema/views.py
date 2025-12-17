import typing

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieCreateUpdateSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionCreateUpdateSerializer,
    ActorFullNameSerializer,
)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorFullNameSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self) -> typing.Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieCreateUpdateSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> typing.Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieSessionCreateUpdateSerializer
        return MovieSessionSerializer
