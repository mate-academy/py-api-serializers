from rest_framework import viewsets

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema.serializers import (
    ActorCreateUpdateSerializer,
    ActorDetailSerializer,
    ActorListSerializer,
    CinemaHallCreateUpdateCapacitySerializer,
    CinemaHallCreateUpdateSerializer,
    CinemaHallDetailSerializer,
    CinemaHallListSerializer,
    GenreCreateUpdateSerializer,
    GenreListNameSerializer,
    GenreListSerializer,
    MovieCreateSerializer,
    MovieDetailSerializer,
    MovieListSerializer,
    MovieSessionCreateSerializer,
    MovieSessionDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionCreateUpdateSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    ordering_fields = ["id", "first_name", "last_name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        if self.action == "retrieve":
            return ActorDetailSerializer
        return ActorCreateUpdateSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    ordering_fields = ["id", "name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        return GenreCreateUpdateSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    ordering_fields = ["id", "name", "rows", "seats_in_row"]

    def get_serializer_class(self):
        if self.action == "list":
            return CinemaHallListSerializer
        if self.action == "retrieve":
            return CinemaHallDetailSerializer
        return CinemaHallCreateUpdateCapacitySerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    ordering_fields = ["id", "title", "description", "duration"]

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    ordering_fields = ["id", "show_time", "movie", "cinema_hall"]

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionCreateSerializer

