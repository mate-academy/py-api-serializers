from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet

from cinema.models import Genre, Actor, CinemaHall, MovieSession, Movie
from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")

        return queryset.all()

    def get_serializer_class(self) -> [MovieSessionListSerializer,
                                       MovieSessionSerializer] :
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")

        return queryset.all()

    def get_serializer_class(self) -> [MovieListSerializer, MovieSerializer] :
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer
