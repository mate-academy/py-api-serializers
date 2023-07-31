from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre, Actor, CinemaHall
)
from cinema.serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
