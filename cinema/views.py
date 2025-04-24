from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
    Order,
    Ticket,
    Actor
)

from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    OrderSerializer,
    TicketSerializer,
    MovieSessionListSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionRetrieveSerializer,
    CinemaHallRetrieveSerializer,
    ActorSerializer
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CinemaHallRetrieveSerializer
        return CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.prefetch_related("genres", "actors")

        return self.queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.select_related("movie", "cinema_hall")

        return self.queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
