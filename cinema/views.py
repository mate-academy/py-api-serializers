from rest_framework import viewsets
from .models import Movie, MovieSession, Genre, Actor, CinemaHall
from .serializers import (
    MovieSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from typing import Type
from rest_framework import serializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> Type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieSessionSerializer
        return MovieSessionDetailSerializer
