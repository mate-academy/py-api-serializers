from rest_framework import viewsets


from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieReadSerializer,
    MovieSessionReadSerializer,
    MovieWriteSerializer,
    MovieSessionListSerializer,
    MovieSessionWriteSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreHallViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return MovieWriteSerializer

        return MovieReadSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = MovieSession.objects

        queryset = queryset.select_related(
            "movie",
            "cinema_hall",
        )

        if self.action == "retrieve":
            queryset = queryset.prefetch_related(
                "movie__genres",
                "movie__actors",
            )

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return MovieSessionWriteSerializer

        return MovieSessionReadSerializer
