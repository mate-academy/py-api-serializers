from rest_framework import viewsets

from cinema.models import (Movie,
                           Genre,
                           Actor,
                           CinemaHall,
                           MovieSession)
from cinema.serializers import (MovieSessionSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.all().prefetch_related(
                "actors",
                "genres")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer

    def get_queryset(self):
        return MovieSession.objects.select_related(
            "movie",
            "cinema_hall"
        ).prefetch_related(
            "movie__genres",
            "movie__actors"
        )
