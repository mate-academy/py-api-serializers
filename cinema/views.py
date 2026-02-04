from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ('list', 'retrieve'):
            return self.queryset.prefetch_related('genres', 'actors')
        return self.queryset.all()


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == 'list':
            return MovieSessionListSerializer
        elif self.action == 'retrieve':
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ('list', 'retrieve'):
            return self.queryset.select_related('movie', 'cinema_hall')
        return self.queryset.all()
