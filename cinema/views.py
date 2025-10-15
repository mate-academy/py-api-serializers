from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets, serializers

from cinema.models import (CinemaHall,
                           Genre,
                           Actor,
                           MovieSession,
                           Movie)
from cinema.serializers import (CinemaHallSerializer,
                                GenreSerializer,
                                ActorSerializer,
                                MovieListSerializer,
                                MovieRetrieveSerializer,
                                MovieSerializer,
                                MovieSessionListSerializer,
                                MovieSessionSerializer,
                                MovieSessionRetrieveSerializer)


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

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return Movie.objects.prefetch_related(
                "actors", "genres"
            )

        return Movie.objects.all()

    def get_serializer_class(
            self
    ) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):

    def get_queryset(self) -> QuerySet:
        if self.action in ("list", "retrieve"):
            return MovieSession.objects.prefetch_related(
                "movie__actors", "movie__genres"
            ).select_related(
                "movie", "cinema_hall"
            )

        return MovieSession.objects.all()

    def get_serializer_class(
            self
    ) -> Type[serializers.Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer
