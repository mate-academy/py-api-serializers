from rest_framework.viewsets import ModelViewSet
from cinema.models import CinemaHall
from cinema.serializers.cinema_hall import CinemaHallSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
