from typing import Type, Optional
from rest_framework.serializers import Serializer
from django.db.models.query import QuerySet
from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    OrderSerializer,
    TicketSerializer,
)


class CinemaHallSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("actors", "genres")
        return queryset


class MovieSessionSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            return queryset.select_related("movie", "cinema_hall")
        return queryset


class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
