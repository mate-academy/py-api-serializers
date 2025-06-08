from rest_framework import mixins, viewsets

from cinema.models import MovieSession, Movie, Actor, Genre, CinemaHall
from cinema.serializers import (
    MovieSessionSerializer,
    MovieSerializer,
    MovieRetrieveSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionRetrieveSerializer,
    MovieListSerializer,
    MovieSessionListSerializer,
    CinemaHallRetrieveSerializer,
    ActorListSerializer,
    MovieSessionCreateSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == ("list", "retrieve"):
            return queryset.prefetch_related(
                "genres",
                "actors",
            )
        else:
            return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionCreateSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()
        else:
            return queryset


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ActorSerializer
        return ActorListSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallRetrieveSerializer
        return CinemaHallSerializer
