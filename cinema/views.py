from rest_framework.viewsets import ModelViewSet

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionListSerializer,
    MovieSessionRetrieveSerializer,
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = MovieSession.objects.all()
        if self.action in ("list", "retrieve"):
            return queryset.select_related("cinema_hall", "movie")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
