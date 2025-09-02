from rest_framework import viewsets, serializers
from django.db import models
from .models import Genre, Actor, CinemaHall, Movie, MovieSession
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieSessionCreateSerializer,
    MovieCreateSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action in ["create", "update", "partial_update"]:
            return MovieCreateSerializer
        return MovieDetailSerializer

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
            return MovieSessionDetailSerializer
        if self.action in ["create", "update", "partial_update"]:
            return MovieSessionCreateSerializer
        return MovieSessionDetailSerializer

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()
