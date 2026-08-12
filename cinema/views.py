from rest_framework import viewsets

from cinema.models import Movie, MovieSession, Actor, CinemaHall, Genre
from cinema.serializers import (MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionSerializer,
                                MovieSessionDetailSerializer,
                                MovieSessionListSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                GenreSerializer)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related(
        "genres",
        "actors",
    )

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset.select_related(
            "movie",
            "cinema_hall",
        )

        if self.action == "retrieve":
            queryset = queryset.prefetch_related(
                "movie__genres",
                "movie__actors",
            )

        return queryset


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
