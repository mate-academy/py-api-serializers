from rest_framework import viewsets

from cinema.models import Actor, Genre, Movie, MovieSession, CinemaHall
from cinema.serializers import (
    ActorListSerializer,
    GenreListSerializer,
    GenreDetailSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    ActorDetailSerializer,
    CinemaHallListSerializer,
    CinemaHallDetailSerializer,
    MovieCreateSerializer,
    MovieSessionCreateSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        else:
            return ActorDetailSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        else:
            return GenreDetailSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related(
        "actors"
    ).prefetch_related("genres")

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related(
                "actors"
            ).prefetch_related("genres")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "cinema_hall"
    ).select_related(
        "movie"
    )

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related(
                "cinema_hall"
            ).prefetch_related(
                "movie"
            )
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        else:
            return MovieSessionCreateSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CinemaHallListSerializer
        else:
            return CinemaHallDetailSerializer
