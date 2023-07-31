from rest_framework import viewsets

from .serializers import (
    CinemaHallSerializers,
    GenreSerializers,
    ActorSerializers,
    MovieSerializers,
    MovieListSerializers,
    MovieDetailSerializers,
    MovieSessionSerializers,
    MovieSessionListSerializers,
    OrderSerializers,
    TicketSerializers,
    MovieSessionDetailSerializers,
)
from .models import (
    CinemaHall,
    Genre,
    Actor,
    MovieSession,
    Movie,
    Order,
    Ticket
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializers

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializers
        elif self.action == "retrieve":
            return MovieSessionDetailSerializers
        return MovieSessionSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related(
        "genres"
    ).prefetch_related(
        "actors"
    )
    serializer_class = MovieSerializers

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializers
        elif self.action == "retrieve":
            return MovieDetailSerializers
        return MovieSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers
