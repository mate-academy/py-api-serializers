from rest_framework import viewsets
from .models import (
    Actor,
    Genre,
    CinemaHall,
    Movie,
    MovieSession
)
from .serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer
)


class ActorViewsSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewsSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewsSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewsSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):

        if self.action == "retrieve":
            return MovieDetailSerializer

        if self.action == "list":
            return MovieListSerializer

        return MovieSerializer


class MovieSessionViewsSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        if self.action == "list":
            return MovieSessionListSerializer

        return MovieSessionSerializer
