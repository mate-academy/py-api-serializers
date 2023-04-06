from rest_framework import viewsets

from cinema.models import Movie, Actor, Genre, CinemaHall
from cinema.serializers import MovieSerializer, MovieListSerializer, ActorSerializer, GenreSerializer, \
    CinemaHallSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_view_name(self):
        if "list" in self.settings.VIEW_NAME_FUNCTION(self):
            return "Cinema Halls"
        return "Cinema Hall Instance"

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        return MovieSerializer
