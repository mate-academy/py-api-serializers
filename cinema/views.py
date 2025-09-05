from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall,
    MovieSession
)
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionWriteSerializer
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
    queryset = Movie.objects.prefetch_related()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type[
        MovieSerializer
        | MovieDetailSerializer
        | MovieWriteSerializer
    ]:
        if self.action == "list":
            return MovieSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieWriteSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type[
        MovieSessionSerializer
        | MovieSessionDetailSerializer
        | MovieSessionWriteSerializer
    ]:
        if self.action == "list":
            return MovieSessionSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
