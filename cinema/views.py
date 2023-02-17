# write views here
from rest_framework.viewsets import ModelViewSet

from cinema.models import Genre,Actor,CinemaHall,Movie,MovieSession
from cinema.serializers import GenreListSerializer, ActorListSerializer, CinemaHallListSerializer, MovieListSerializer, \
    MovieSessionSerializer, MovieDetailSerializer, MovieSessionDetailSerializer, ActorDetailSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        return ActorDetailSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallListSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer

class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionSerializer
        return MovieSessionDetailSerializer