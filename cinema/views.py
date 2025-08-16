from rest_framework import viewsets
from .models import CinemaHall, Genre, Actor, Movie, MovieSession
from .serializers import (CinemaHallSerializer,
                          GenreSerializer,
                          ActorSerializer,
                          MovieListSerializer,
                          MovieDetailSerializer,
                          MovieSessionListSerializer,
                          MovieSessionDetailSerializer)


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
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related(
        "movie",
        "cinema_hall"
    )
    serializer_class = MovieSessionListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
