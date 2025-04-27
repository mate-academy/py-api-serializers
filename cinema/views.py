from rest_framework import viewsets
from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)
from .serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer, MovieListSerializer,
    MovieSessionListSerializer, MovieCreateSerializer,
    MovieSessionCreateSerializer,
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
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieCreateSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionSerializer
        return MovieSessionCreateSerializer
