from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
    Actor,
    Order,
    Ticket,
)
from cinema.serializers import (
    CinemaHallSerializer, GenreSerializer, ActorSerializer, MovieSerializer,
    MovieSessionSerializer, OrderSerializer, TicketSerializer,
    MovieSessionListSerializer, MovieListSerializer,
    MovieSessionDetailsSerializer, MovieDetailSerializer,
)


class CinemaHallViewSet(ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieDetailSerializer
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return MovieSessionSerializer
        if self.action == "retrieve":
            return MovieSessionDetailsSerializer
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailsSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
