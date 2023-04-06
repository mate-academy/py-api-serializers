from rest_framework import viewsets

from cinema.models import Movie
from cinema.serializers import MovieSerializer, MovieListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors", "genres")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        return MovieSerializer

