from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor
from cinema.serializers import CinemaHallSerializer, GenreSerializer, \
    ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
