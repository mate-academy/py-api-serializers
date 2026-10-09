from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, CinemaHall, Genre, Actor, MovieSession
from cinema.serializers import (MovieListSerializer,
                                MovieDetailSerializer,
                                MovieBaseSerializer,
                                CinemaHallSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionBaseSerializer)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "list":
                return MovieListSerializer
            case "retrieve":
                return MovieDetailSerializer
            case _:
                return MovieBaseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ("list", "retrieve"):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")

    def get_serializer_class(self):
        match self.action:
            case "list":
                return MovieSessionListSerializer
            case "retrieve":
                return MovieSessionDetailSerializer
            case _:
                return MovieSessionBaseSerializer
