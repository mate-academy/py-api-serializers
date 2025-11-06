from rest_framework.viewsets import ModelViewSet
from cinema.models import Movie
from cinema.serializers.movie import MovieListSerializer, MovieDetailSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer
