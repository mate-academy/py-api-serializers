from rest_framework.viewsets import ModelViewSet

from cinema.models import Genre, Actor, CinemaHall, Movie
from cinema.serializers import GenreSerializer, ActorSerializer, CinemaHallSerializer, MovieSerializer, \
    MovieListSerializer, MovieRetrieveSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        if self.action in ["list", "retrieve"]:
            return Movie.objects.all().prefetch_related("genres", "actors")
        return Movie.objects.all()
