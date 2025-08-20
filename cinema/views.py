from rest_framework import viewsets
from .models import (Genre, Actor, CinemaHall,
                     Movie, MovieSession)
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    CinemaHallDetailSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieWriteSerializer,
    MovieSessionWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallDetailSerializer
        return CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres",
                                              "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieWriteSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie",
                                                   "cinema_hall")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionWriteSerializer
