# write views here
from rest_framework import viewsets, serializers

from cinema.models import Genre, CinemaHall, Actor, Movie, MovieSession
from cinema.serializers import (GenreSerializer, CinemaHallSerializer,
                                ActorSerializer,
                                MovieSessionListSerializer,
                                MovieListSerializer,
                                MovieCreateUpdateSerializer,
                                MovieDetailSerializer,
                                MovieSessionCreateSerializer,
                                MovieSessionDetailSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related(
        "genres", "actors"
    ).all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieCreateUpdateSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionListSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset
