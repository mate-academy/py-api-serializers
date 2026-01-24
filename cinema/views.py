from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Genre, Actor, CinemaHall, Movie, MovieSession, Order, Ticket
from .serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
    OrderSerializer,
    TicketSerializer,
)

# Para todas as entidades simples, podemos usar AllowAny (assumindo que não há autenticação obrigatória para CRUD simples)
class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
    permission_classes = [AllowAny]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]

# View para Movie (diferentes serializers para list e detail)
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieDetailSerializer

# View para MovieSession (diferentes serializers para list e detail)
class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer

# Views para Order e Ticket (usando os serializers base)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]
