from rest_framework import viewsets

from cinema.models import CinemaHall
from cinema.serializers import CinemaHallSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()
