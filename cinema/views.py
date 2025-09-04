from rest_framework import viewsets
import rest_framework.serializers as drf_serializers

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession
)
from cinema.serializers import (
    MovieSessionSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    MovieCreateSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[drf_serializers.Serializer]:
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieSerializer
        return MovieCreateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        MovieSession.objects.select_related("cinema_hall", "movie")
        .prefetch_related("movie__genres", "movie__actors")
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[drf_serializers.Serializer]:
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionSerializer
