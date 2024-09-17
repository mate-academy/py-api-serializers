from rest_framework import viewsets

from cinema.models import (
    Movie,
    MovieSession,
    Genre,
    CinemaHall,
    Actor
)
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    ActorSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("actors", "genres")

        return queryset

    serializers = {
        "list": MovieListSerializer,
        "retrieve": MovieDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, MovieSerializer)


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("movie", "cinema_hall")

        return queryset

    serializers = {
        "list": MovieSessionListSerializer,
        "retrieve": MovieSessionDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, MovieSessionSerializer)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
