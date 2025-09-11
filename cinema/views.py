from typing import Type
from django.db.models import QuerySet
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionWriteSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AllowAny,)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by("id")
    serializer_class = ActorSerializer
    permission_classes = (AllowAny,)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieWriteSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self) -> QuerySet:
        return Movie.objects.prefetch_related("actors", "genres")

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieWriteSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSessionWriteSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self) -> QuerySet:
        if self.action == "list":
            return (
                MovieSession.objects
                .select_related("movie", "cinema_hall")
                .order_by("-show_time")
            )
        if self.action == "retrieve":
            return (
                MovieSession.objects
                .select_related("movie", "cinema_hall")
                .prefetch_related("movie__actors", "movie__genres")
                .order_by("-show_time")
            )
        return MovieSession.objects.all().order_by("-show_time")

    def get_serializer_class(self) -> Type[serializers.BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
