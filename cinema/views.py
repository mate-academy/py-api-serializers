from rest_framework import viewsets

from cinema.models import (
    CinemaHall,
    Genre
)
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
