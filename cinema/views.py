from rest_framework.viewsets import GenericViewSet, ModelViewSet


from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    MovieListSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieDetailSerializer,
)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return self.serializer_class


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
