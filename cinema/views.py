from rest_framework import viewsets
from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)
from .serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer,
    MovieListSerializer, MovieDetailReadSerializer,
    MovieDetailWriteSerializer, MovieSessionListSerializer,
    MovieSessionDetailReadSerializer, MovieSessionDetailWriteSerializer
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
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self) -> type:
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieDetailWriteSerializer
        return MovieDetailReadSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie", "cinema_hall"
    ).prefetch_related(
        "movie__genres", "movie__actors"
    )

    def get_serializer_class(self) -> type:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieSessionDetailWriteSerializer
        return MovieSessionDetailReadSerializer
