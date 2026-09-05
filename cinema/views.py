from django.db.models import QuerySet
from cinema.serializers import (CinemaHallSerializer, GenreSerializer,
                                ActorSerializer, MovieSerializer,
                                MovieSessionSerializer, OrderSerializer,
                                TicketSerializer, TicketListSerializer,
                                OrderListSerializer,
                                MovieSessionListSerializer,
                                MovieListSerializer, TicketRetrieveSerializer,
                                OrderRetrieveSerializer,
                                MovieSessionRetrieveSerializer,
                                MovieRetrieveSerializer)
from cinema.models import (CinemaHall, Genre, Actor, Movie,
                           MovieSession, Order, Ticket)
from rest_framework import viewsets
from rest_framework.serializers import Serializer


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
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> Serializer[MovieListSerializer
                                                 | MovieRetrieveSerializer
                                                 | MovieSerializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer

        return MovieSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")

        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) \
            -> Serializer[MovieSessionSerializer
                          | MovieSessionListSerializer
                          | MovieSessionRetrieveSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer

        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return (queryset.select_related(
                "movie", "cinema_hall").prefetch_related(
                "movie__genres", "movie__actors"))

        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self) -> Serializer[OrderListSerializer
                                                 | OrderRetrieveSerializer
                                                 | OrderSerializer]:
        if self.action == "list":
            return OrderListSerializer
        elif self.action == "retrieve":
            return OrderRetrieveSerializer

        return OrderSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()

        return queryset


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self) -> Serializer[TicketListSerializer
                                                 | TicketRetrieveSerializer
                                                 | TicketSerializer]:
        if self.action == "list":
            return TicketListSerializer
        elif self.action == "retrieve":
            return TicketRetrieveSerializer

        return TicketSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset

        if self.action in ("list", "retrieve"):
            return queryset.select_related()

        return queryset
