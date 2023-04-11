from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Actor, Genre, CinemaHall
from cinema.serializers import (MovieListSerializer,
                                MovieSerializer,
                                MovieDetailSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                ActorSerializer,
                                GenreSerializer,
                                CinemaHallSerializer)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("cinema_hall")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer


class ActorSessionViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreSessionViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallSessionViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
