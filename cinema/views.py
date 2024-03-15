from rest_framework import viewsets

from .models import (
    Movie,
    Actor,
    Genre,
    MovieSession,
    CinemaHall,
)
from .serializers import (
    MovieSerializer,
    MovieDetailSerializer,
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action not in ("list", "retrieve"):
            return self.queryset
        return self.queryset.prefetch_related("genres__movies__actors")


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
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action not in ("list", "retrieve"):
            return self.queryset
        return self.queryset.select_related("cinema_hall", "movie")
