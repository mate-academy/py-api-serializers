from rest_framework import viewsets

from cinema.models import CinemaHall
from cinema.serializers import CinemaHallSerializer


class CinemaHallView(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
