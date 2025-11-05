from rest_framework import viewsets
from cinema.models import Genre, Movie, Actor, CinemaHall, MovieSession
from cinema.serializers import (MovieSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer,
                                CinemaHallSerializer,
                                ActorSerializer,
                                GenreSerializer,
                                )


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
    queryset = MovieSession.objects
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list" or self.action == "retrieve":
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list" or self.action == "retrieve":
            queryset = queryset.prefetch_related("actors", "genres")
        return queryset
