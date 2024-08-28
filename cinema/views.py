from rest_framework import viewsets, serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return self.serializer_class


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie").select_related(
        "cinema_hall"
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer
