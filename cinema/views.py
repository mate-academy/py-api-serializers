from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Genre.objects.all()
    serializer_class: Type[Serializer] = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Actor.objects.all()
    serializer_class: Type[Serializer] = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = CinemaHall.objects.all()
    serializer_class: Type[Serializer] = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset: QuerySet = MovieSession.objects.select_related(
        "movie",
        "cinema_hall"
    )

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
