from typing import Type

from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from cinema.models import (
    Genre,
    Actor,
    Movie,
    CinemaHall,
    MovieSession,
    Order,
    Ticket
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    CinemaHallSerializer,
    MovieSessionSerializer,
    OrderSerializer,
    TicketSerializer,
    OrderListSerializer,
    TicketListSerializer,
    MovieSessionListSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Movie] = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self) -> QuerySet[Movie]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return (queryset
                    .prefetch_related("genres")
                    .prefetch_related("actors"))
        return queryset


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[MovieSession] = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self) -> QuerySet[MovieSession]:
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Order] = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return OrderListSerializer
        return OrderSerializer

    def get_queryset(self) -> QuerySet[Order]:
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("user")
        return queryset


class TicketViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Ticket] = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return TicketListSerializer
        return TicketSerializer

    def get_queryset(self) -> QuerySet[Ticket]:
        queryset = self.queryset
        if self.action == "list":
            queryset = (queryset
                        .select_related("movie_session", "order"))
        return queryset
