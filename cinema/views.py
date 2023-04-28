from rest_framework import viewsets

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall
)
from cinema.serializers import (
    MovieSerializer,
    MovieRetrieveSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieListSerializer,
    CinemaHallSerializer
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
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer
