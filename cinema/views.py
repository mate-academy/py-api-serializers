from rest_framework import viewsets

from cinema.models import (
    Movie,
    MovieSession,
    CinemaHall,
    Genre,
    Actor
)
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related("actors", "genres")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all().select_related(
        "movie",
    ).select_related("cinema_hall")
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
