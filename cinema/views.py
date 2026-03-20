from typing import Type, Any

from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet

from cinema.models import (CinemaHall, Actor, Genre, Movie, MovieSession)
from cinema.serializers import (CinemaHallSerializer, GenreSerializer,
                                MovieSessionSerializer, MovieListSerializer, MovieDetailSerializer,
                                MovieDetailPostSerializer, MovieSessionDetailSerializer, ActorDetailSerializer,
                                MovieSessionPostSerializer)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorsViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset: QuerySet = Movie.objects.all()

    def get_queryset(self) -> QuerySet:
        if self.action in ["list", "retrieve"]:
            return Movie.objects.prefetch_related('genres', 'actors')
        return Movie.objects.all()

    def get_serializer_class(self) -> Type[Any]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieDetailPostSerializer
        return MovieListSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset: QuerySet = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[Any]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ["create", "update", "partial_update"]:
            return MovieSessionPostSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        if self.action in ["list", "retrieve"]:
            return MovieSession.objects.select_related("movie", "cinema_hall")
        return MovieSession.objects.all()
