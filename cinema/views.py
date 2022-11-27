from rest_framework import viewsets

from cinema.models import (
    Movie,
    MovieSession,
    Actor,
    Genre,
    CinemaHall,
)
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
)


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> type(serializer_class):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie",
        "cinema_hall"
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> type(serializer_class):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
