from rest_framework import viewsets

from cinema.models import CinemaHall, Movie
from cinema.serializers import CinemaHallSerializer, MovieSerializer, MovieListSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):

        if self.action == 'list':
            return MovieListSerializer
        return MovieSerializer
