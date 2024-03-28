from rest_framework import viewsets

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related('genres', 'actors')
    serializer_class = MovieSerializer
