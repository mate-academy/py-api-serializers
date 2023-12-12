from rest_framework.viewsets import ModelViewSet


from cinema.models import Movie, MovieSession, CinemaHall, Actor, Genre
from cinema.serializers import (MovieSerializer,
                                MovieListSerializer,
                                MovieDetailSerializer,
                                MovieSessionSerializer,
                                MovieSessionListSerializer,
                                MovieSessionDetailSerializer,
                                CinemaHallSerializer,
                                ActorSerializer,
                                GenreSerializer)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
