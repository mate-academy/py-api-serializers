from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession
from cinema.serializers import (MovieDetailSerializer,
                                MovieListSerializer,
                                MovieSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSessionSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionListSerializer)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


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
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionSerializer
