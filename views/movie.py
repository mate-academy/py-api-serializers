from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from cinema.models import Movie
from cinema.serializers.movie import MovieListSerializer, MovieDetailSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "actors")  # Optimized queryset

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieListSerializer
        return MovieDetailSerializer
