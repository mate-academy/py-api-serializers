from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieCreateSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieSessionCreateSerializer,
    MovieSessionListSerializer,
    MovieSessionSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    serializer_action_classes = {
        "list": MovieListSerializer,
        "create": MovieCreateSerializer,
        "retrieve": MovieSerializer,
        "update": MovieSerializer,
        "partial_update": MovieSerializer,
        "destroy": MovieSerializer,
    }

    def get_serializer_class(self) -> Type[BaseSerializer]:
        return self.serializer_action_classes.get(self.action, MovieSerializer)

    def get_queryset(self) -> QuerySet[Movie]:
        if self.action in ["list", "retrieve"]:
            return self.queryset.prefetch_related("genres", "actors")
        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    serializer_action_classes = {
        "list": MovieSessionListSerializer,
        "create": MovieSessionCreateSerializer,
        "retrieve": MovieSessionSerializer,
        "update": MovieSessionSerializer,
        "partial_update": MovieSessionSerializer,
        "destroy": MovieSessionSerializer,
    }

    def get_serializer_class(self) -> Type[BaseSerializer]:
        return self.serializer_action_classes.get(self.action,
                                                  MovieSessionSerializer)

    def get_queryset(self) -> QuerySet[MovieSession]:
        if self.action == "list":
            return self.queryset.select_related("movie", "cinema_hall")
        if self.action == "retrieve":
            return self.queryset.prefetch_related(
                "movie__genres",
                "movie__actors",
                "cinema_hall"
            )
        return self.queryset
