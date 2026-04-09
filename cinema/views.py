from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.serializers import (GenreSerializer,
                                ActorSerializer,
                                CinemaHallSerializer,
                                MovieDetailSerializer,
                                MovieSessionListSerializer,
                                MovieListSerializer,
                                MovieSessionDetailSerializer,
                                MovieCreateSerializer,
                                MovieSessionCreateSerializer)
from cinema.models import (Genre,
                           Actor,
                           CinemaHall,
                           Movie,
                           MovieSession)


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
    queryset = Movie.objects
    serializer_class = MovieDetailSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieCreateSerializer
        return MovieDetailSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects
    serializer_class = MovieSessionDetailSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

    def get_serializer_class(self) -> type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        if self.action in ("create", "update", "partial_update"):
            return MovieSessionCreateSerializer
        return MovieSessionDetailSerializer
