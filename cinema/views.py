"""CRUD viewsets with action-specific read representations."""
from __future__ import annotations

from django.db.models import QuerySet
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionSerializer,
)


class GenreViewSet(ModelViewSet):
    """Manage genres."""

    queryset: QuerySet[Genre] = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    """Manage actors."""

    queryset: QuerySet[Actor] = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    """Manage screening rooms."""

    queryset: QuerySet[CinemaHall] = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    """Use string lists, nested details, or writable IDs by action."""

    queryset: QuerySet[Movie] = Movie.objects.prefetch_related(
        "genres", "actors"
    )
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    """Provide session summaries, nested details, and ID-based writes."""

    queryset: QuerySet[MovieSession] = (
        MovieSession.objects.select_related("movie", "cinema_hall")
        .prefetch_related("movie__genres", "movie__actors")
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer
